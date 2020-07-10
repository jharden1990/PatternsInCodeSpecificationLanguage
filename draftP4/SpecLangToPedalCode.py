__author__ = "jessemh"

import sys
from antlr4 import *
from antlr4.InputStream import InputStream
import re


from specLang_draftP4Lexer import specLang_draftP4Lexer
from specLang_draftP4Parser import specLang_draftP4Parser
from specLang_draftP4ParserListener import specLang_draftP4ParserListener

class SpecLangToPedalCodeTranslator(specLang_draftP4ParserListener):
    def __init__(self):
        self.translation_string = ""
        self.num_findclause = 0
        self.num_whereclause = 0
        self.num_withinclause = 0
        self.exp_match1 = re.compile('__[^ ]+__')  # /regex
        #self.exp_match2 = re.compile('__[^ ]+__$')
        self.var_match1 = re.compile('_[^ _]+_')  # /regex
        #self.var_match2 = re.compile('_[^ _]+_$')
        #self.var_match3 = re.compile(' _[^ _]+_ ')
        self.general_match_start = re.compile('^(_[0-9a-zA-Z_]*_)(?:[^0-9a-zA-Z_])')
        self.general_match_end = re.compile('(?:[^0-9a-zA-Z_])(_[0-9a-zA-Z_]*_)$')
        self.general_match_middle = re.compile('(?:[^0-9a-zA-Z_])(_[0-9a-zA-Z_]*_)(?:[^0-9a-zA-Z_])')
        self.exp_match2 = re.compile('^__[0-9a-zA-Z_]*__$')
        self.wildcard_match = re.compile('^___$')
        self.var_match2 = re.compile('^_[0-9a-zA-Z_]*_$')


    def getTranslationString(self):
        return self.translation_string

    def updateTranslationString(self, string_value):
        self.translation_string += string_value

    def enterDocument(self, ctx:specLang_draftP4Parser.DocumentContext):
        self.updateTranslationString("from pedal.quick import *\n\n")

    def exitBeginpart(self, ctx:specLang_draftP4Parser.BeginpartContext):
        string_to_add = "\ndef " + ctx.NAME().getText() + "("
        num_tokens_processed = 1
        for parens_token in ctx.PARENS_TEXT():
            string_to_add += parens_token.getText()
            if num_tokens_processed < len(ctx.PARENS_TEXT()):
                string_to_add += ", "
                num_tokens_processed = num_tokens_processed + 1
        string_to_add += "):\n"
        self.updateTranslationString(string_to_add)
        self.num_findclause = 0
        self.num_whereclause = 0
        self.num_withinclause = 0

    def exitMessagepart(self, ctx:specLang_draftP4Parser.MessagepartContext):
        string_to_add = "\tMESSAGE= '" + ctx.CODE_TEXT().getText() + "'\n"
        self.updateTranslationString(string_to_add)

    def exitLabelpart(self, ctx:specLang_draftP4Parser.LabelpartContext):
        string_to_add = "\tLABEL = '" + ctx.CODE_TEXT().getText() + "'\n"
        self.updateTranslationString(string_to_add)

    def exitTitlepart(self, ctx:specLang_draftP4Parser.TitlepartContext):
        string_to_add = "\tTITLE = '" + ctx.CODE_TEXT().getText() + "'\n"
        self.updateTranslationString(string_to_add)

    def exitFindclause(self, ctx:specLang_draftP4Parser.FindclauseContext):
        this_find = "find" + str(self.num_findclause)
        string_to_add = "\t" + this_find + " = "
        if self.num_findclause == 0:
            string_to_add += "find_matches('" + ctx.CODE_TEXT().getText() + "')\n\tprev_matchset = " + this_find + "\n"
            self.num_findclause += 1
        else:
            string_to_add += "[]\n\tfor match in prev_matchset:\n\t\t" + this_find + ".extend(find_matches('"
            string_to_add += ctx.CODE_TEXT().getText() + "', prev_match = match))"
            string_to_add += "\n\tprev_matchset = " + this_find + "\n"
            self.num_findclause += 1
        self.updateTranslationString(string_to_add)

    def exitWhereclause(self, ctx:specLang_draftP4Parser.WhereclauseContext):
        this_where = "where" + str(self.num_whereclause)
        this_where_pattern = ctx.CODE_TEXT().getText()
        this_where_pattern_for_finding = ctx.CODE_TEXT().getText()
        #print(this_where_pattern)
        generals_found = self.general_match_start.findall(this_where_pattern)
        generals_found.extend(self.general_match_end.findall(this_where_pattern))
        generals_found.extend(self.general_match_middle.findall(this_where_pattern))
        # remove duplicates by transforming the list into a set; then transform the non-duplicate set back into a list.
        generals_found = list(set(generals_found))
        if '___' in generals_found:
            generals_found.remove('___')
        expressions = []
        variables = []
        for general_found in generals_found:
            if self.exp_match2.match(general_found):
                expressions.append(general_found)
            else:
                if self.var_match2.match(general_found):
                    variables.append(general_found)
        #exprs_found = self.exp_match1.findall(this_where_pattern_for_finding)
        #this_where_pattern_for_finding = self.exp_match1.sub("",this_where_pattern_for_finding)
        #vars_found = self.var_match1.findall(this_where_pattern_for_finding)
        # remove duplicates by transforming the list into a set; then transform the non-duplicate set back into a list.
        #exprs_found = list(set(exprs_found))
        #vars_found = list(set(vars_found))
        string_to_add = "\t" + this_where + " = []\n\tfor match in prev_matchset:\n\t\t"
        for var_found in variables:
            #var_found = var_found.strip()
            string_to_add += var_found + " = match['" + var_found + "']\n\t\t"
        for expr_found in expressions:
            #expr_found = expr_found.strip()
            string_to_add += expr_found + " = match['" + expr_found + "']\n\t\t"
        string_to_add += "if " + this_where_pattern + ":\n\t\t\t" + this_where + ".append(match)\n\t"
        string_to_add += "prev_matchset = " + this_where + "\n"
        self.num_whereclause += 1
        self.updateTranslationString(string_to_add)

    def exitWithinclause(self, ctx:specLang_draftP4Parser.WithinclauseContext):
        this_within = "within" + str(self.num_withinclause)
        this_expr = ctx.EXPRESSION().getText()
        string_to_add = "\t" + this_within + " = []\n\tfor match in prev_matchset:\n\t\t"
        string_to_add += this_expr + " = match['" + this_expr + "']\n\t\t"
        string_to_add += this_within + ".extend(" + this_expr + ".find_matches('" + ctx.CODE_TEXT().getText()
        string_to_add += "', use_previous = match))"
        string_to_add += "\n\tprev_matchset = " + this_within + "\n"
        self.num_withinclause += 1
        self.updateTranslationString(string_to_add)

    def exitIfclause(self, ctx:specLang_draftP4Parser.IfclauseContext):
        string_to_add = "\tif "
        if ctx.NOT():
            string_to_add += "not "
        string_to_add += "prev_matchset:\n\t\t"
        if ctx.feedbackpart().NO():
            string_to_add += "return False\n"
        else:
            # feedback within parens processing start
            feedbackparenstext = "("
            if ctx.feedbackpart().feedbackparenspart():
                PARENS_TEXT_TOKENS = ctx.feedbackpart().feedbackparenspart().PARENS_TEXT()
                index = 1
                for PARENS_TEXT_TOKEN in PARENS_TEXT_TOKENS:
                    feedbackparenstext += PARENS_TEXT_TOKEN.getText()
                    if index < len(PARENS_TEXT_TOKENS):
                        feedbackparenstext += ", "
                        index += 1
                CODE_TEXT_TOKENS = ctx.feedbackpart().feedbackparenspart().CODE_TEXT()
                index = 1
                if len(PARENS_TEXT_TOKENS) > 0 and len(CODE_TEXT_TOKENS) > 0:
                    feedbackparenstext += ", "
                for CODE_TEXT_TOKEN in CODE_TEXT_TOKENS:
                    feedbackparenstext += CODE_TEXT_TOKEN.getText()
                    if index < len(CODE_TEXT_TOKENS):
                        feedbackparenstext += ", "
                        index += 1
                feedbackparenstext += ")"
            else:
                feedbackparenstext += "message=MESSAGE, label=LABEL, title=TITLE)"
            # feedback within parens processing end

            if ctx.feedbackpart().GENTLE():
                string_to_add += "return gently" + feedbackparenstext + "\n"
            else:
                string_to_add += "return explain" + feedbackparenstext + "\n"

        # handle elsepart if it exists
        if ctx.elsepart():
            string_to_add += "\telse:\n\t\t"
            if ctx.elsepart().feedbackpart().NO():
                string_to_add += "return False\n"
            else:
                # feedback within parens processing start
                feedbackparenstext = "("
                if ctx.elsepart().feedbackpart().feedbackparenspart():
                    PARENS_TEXT_TOKENS = ctx.elsepart().feedbackpart().feedbackparenspart().PARENS_TEXT()
                    index = 1
                    for PARENS_TEXT_TOKEN in PARENS_TEXT_TOKENS:
                        feedbackparenstext += PARENS_TEXT_TOKEN.getText()
                        if index < len(PARENS_TEXT_TOKENS):
                            feedbackparenstext += ", "
                            index += 1
                    CODE_TEXT_TOKENS = ctx.elsepart().feedbackpart().feedbackparenspart().CODE_TEXT()
                    index = 1
                    if len(PARENS_TEXT_TOKENS) > 0 and len(CODE_TEXT_TOKENS) > 0:
                        feedbackparenstext += ", "
                    for CODE_TEXT_TOKEN in CODE_TEXT_TOKENS:
                        feedbackparenstext += CODE_TEXT_TOKEN.getText()
                        if index < len(CODE_TEXT_TOKENS):
                            feedbackparenstext += ", "
                            index += 1
                    feedbackparenstext += ")"
                else:
                    feedbackparenstext += "message=MESSAGE, label=LABEL, title=TITLE)"
                    # feedback within parens processing end

                if ctx.elsepart().feedbackpart().GENTLE():
                    string_to_add += "return gently" + feedbackparenstext + "\n"
                else:
                    string_to_add += "return explain" + feedbackparenstext + "\n"
        self.updateTranslationString(string_to_add)

    def exitEndpart(self, ctx:specLang_draftP4Parser.EndpartContext):
        string_to_add = "\t"
        if ctx.WITH():
            # feedback within parens processing start
            feedbackparenstext = "("
            if ctx.feedbackparenspart():
                PARENS_TEXT_TOKENS = ctx.feedbackparenspart().PARENS_TEXT()
                index = 1
                for PARENS_TEXT_TOKEN in PARENS_TEXT_TOKENS:
                    feedbackparenstext += PARENS_TEXT_TOKEN.getText()
                    if index < len(PARENS_TEXT_TOKENS):
                        feedbackparenstext += ", "
                        index += 1
                CODE_TEXT_TOKENS = ctx.feedbackparenspart().CODE_TEXT()
                index = 1
                if len(PARENS_TEXT_TOKENS) > 0 and len(CODE_TEXT_TOKENS) > 0:
                    feedbackparenstext += ", "
                for CODE_TEXT_TOKEN in CODE_TEXT_TOKENS:
                    feedbackparenstext += CODE_TEXT_TOKEN.getText()
                    if index < len(CODE_TEXT_TOKENS):
                        feedbackparenstext += ", "
                        index += 1
                feedbackparenstext += ")"
            else:
                feedbackparenstext += "message=MESSAGE, label=LABEL, title=TITLE)"
            # feedback within parens processing end

            if ctx.GENTLE():
                string_to_add += "return gently" + feedbackparenstext + "\n\n"
            else:
                string_to_add += "return explain" + feedbackparenstext + "\n\n"
        else:
            string_to_add += "return False\n\n"
        self.updateTranslationString(string_to_add)

# should the command be "python name_of_script.py output_file input_file", which allows inputStream to output a file?
# should it instead be "python name_of_script.py input_file output_file", which doesn't allow inputStream to output a file?
# there's probably another way to handle it, like checking if either of the files exists and creating the non-existant one?
if __name__ == '__main__':
    if len(sys.argv) > 1: # len(sys.argv) > 2 means output_file then input_file
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = specLang_draftP4Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = specLang_draftP4Parser(token_stream)
    tree = parser.document()

    #lisp_tree_str = tree.toStringTree(recog=parser)
    #print(lisp_tree_str)

    # listener
    print("Start Walking...")
    listener = SpecLangToPedalCodeTranslator()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    final_string = listener.getTranslationString()
    if len(sys.argv) < 3:
        print(final_string)
    else:
        text_file = open(sys.argv[2], "w")
        n = text_file.write(final_string)
        text_file.close()








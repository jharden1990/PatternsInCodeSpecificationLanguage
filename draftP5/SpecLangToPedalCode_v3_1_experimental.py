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
        self.function_list = []
        self.message_list = []

    def get_function_list(self):
        return self.function_list

    def get_message_list(self):
        return self.message_list

    def getTranslationString(self):
        return self.translation_string

    def updateTranslationString(self, string_value):
        self.translation_string += string_value

    def enterDocument(self, ctx:specLang_draftP4Parser.DocumentContext):
        self.updateTranslationString("from pedal.environments.quick import *\n\n")

    def exitBeginpart(self, ctx:specLang_draftP4Parser.BeginpartContext):
        string_to_add = "\ndef "
        function_name = "" + ctx.NAME().getText() + "("
        num_tokens_processed = 1
        for parens_token in ctx.PARENS_TEXT():
            function_name += parens_token.getText()
            if num_tokens_processed < len(ctx.PARENS_TEXT()):
                function_name += ", "
                num_tokens_processed = num_tokens_processed + 1
        function_name += ")"
        self.function_list.append(function_name)
        string_to_add = string_to_add + function_name + ":\n"
        self.updateTranslationString(string_to_add)
        self.num_findclause = 0
        self.num_whereclause = 0
        self.num_withinclause = 0

    def exitMessagepart(self, ctx:specLang_draftP4Parser.MessagepartContext):
        message_string = "" + ctx.CODE_TEXT().getText() + ""
        self.message_list.append(message_string)
        string_to_add = "\tMESSAGE = '" + message_string + "'\n"
        self.updateTranslationString(string_to_add)

    def exitLabelpart(self, ctx:specLang_draftP4Parser.LabelpartContext):
        string_to_add = "\tLABEL = '" + ctx.CODE_TEXT().getText() + "'\n"
        self.updateTranslationString(string_to_add)

    def exitTitlepart(self, ctx:specLang_draftP4Parser.TitlepartContext):
        string_to_add = "\tTITLE = '" + ctx.CODE_TEXT().getText() + "'\n"
        self.updateTranslationString(string_to_add)

    def check_if_found(self, match_list):
        string_to_add = 'if ' + match_list + ':\n\t\tprev_found_matchset = ' + match_list + '\n'
        return string_to_add

    def exitFindclause(self, ctx:specLang_draftP4Parser.FindclauseContext):
        this_find = "find" + str(self.num_findclause)
        string_to_add = "\t" + this_find + " = "
        if self.num_findclause == 0:
            string_to_add += 'find_matches("""' + ctx.CODE_TEXT().getText() + '""")\n\tprev_matchset = ' + this_find + "\n\t"
            string_to_add += 'prev_found_matchset = []\n\t'
            string_to_add += self.check_if_found(this_find)
            self.num_findclause += 1
        else:
            string_to_add += "[]\n\tfor match in prev_matchset:\n\t\t" + this_find + '.extend(find_matches("""'
            string_to_add += ctx.CODE_TEXT().getText() + '""", use_previous = match))'
            string_to_add += "\n\tprev_matchset = " + this_find + "\n"
            string_to_add += self.check_if_found(this_find)
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
        string_to_add += "prev_matchset = " + this_where + "\n\t"
        string_to_add += self.check_if_found(this_where)
        self.num_whereclause += 1
        self.updateTranslationString(string_to_add)

    def exitWithinclause(self, ctx:specLang_draftP4Parser.WithinclauseContext):
        this_within = "within" + str(self.num_withinclause)
        this_expr = ctx.EXPRESSION().getText()
        string_to_add = "\t" + this_within + " = []\n\tfor match in prev_matchset:\n\t\t"
        string_to_add += this_expr + " = match['" + this_expr + "']\n\t\t"
        string_to_add += this_within + ".extend(" + this_expr + '.find_matches("""' + ctx.CODE_TEXT().getText()
        string_to_add += '""", use_previous = match))'
        string_to_add += "\n\tprev_matchset = " + this_within + "\n\t"
        string_to_add += self.check_if_found(this_within)
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
                feedbackparenstext += "message=MESSAGE.format(**prev_found_matchset[0].names()), label=LABEL, title=TITLE)"
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
                    feedbackparenstext += "message=MESSAGE.format(**prev_found_matchset[0].names()), label=LABEL, title=TITLE)"
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
                feedbackparenstext += "message=MESSAGE.format(**prev_found_matchset[0].names()), label=LABEL, title=TITLE)"
            # feedback within parens processing end

            if ctx.GENTLE():
                string_to_add += "return gently" + feedbackparenstext + "\n\n"
            else:
                string_to_add += "return explain" + feedbackparenstext + "\n\n"
        else:
            string_to_add += "return False\n\n"
        self.updateTranslationString(string_to_add)

    def make_unit_test_string(self, name_of_file):
        unit_test_string = "import unittest\nimport ast\nimport sys\nimport os\n\n\n\n"
        # may need to add this back in: \nos.environ['PEDAL_AS_LIBRARY'] = \"1\"
        unit_test_string = unit_test_string + "sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\n\n"
        unit_test_string = unit_test_string + "from pedal import contextualize_report\n"
        unit_test_string += "from pedal.cait.cait_api import *\nfrom pedal.core.report import MAIN_REPORT\n"
        unit_test_string += "from pedal.source import set_source, verify\nfrom pedal.tifa import tifa_analysis\n"
        unit_test_string += "from " + name_of_file.replace(".py", "") + " import *\n\n\nclass MistakeTest(unittest.TestCase):\n"
        unit_test_string += "\tSUBMISSION_STRING = ''\n\n\t@staticmethod\n\t"
        unit_test_string += "def to_source(source):\n\t\tMAIN_REPORT.clear()\n\t\t"
        unit_test_string += "contextualize_report(source)\n\t\tverify()\n\t\tparse_program()\n\t\t"
        unit_test_string += "tifa_analysis()\n\n\tdef setUp(self):\n\t\tself.to_source(self.SUBMISSION_STRING)\n\n\t"
        for function_name, message_text in zip(self.function_list, self.message_list):
            test_function_name = function_name.replace("(", "(self, ")
            unit_test_string += "def test_" + test_function_name + ":\n\t\tself.assertFalse("
            unit_test_string += "" + function_name + ", '" + message_text + "')\n\n\t"
        unit_test_string += "\n\nif __name__ == \"__main__\":\n\tif len(sys.argv) > 1:\n\t\t"
        unit_test_string += "potential_file = sys.argv.pop()\n\t\tif os.path.isfile(potential_file):\n\t\t\t"
        unit_test_string += "with open(potential_file, 'r') as read_file:\n\t\t\t\tMistakeTest.SUBMISSION_STRING = "
        unit_test_string += "read_file.read()\n\tunittest.main()"
        return unit_test_string


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
        if len(sys.argv) > 3:
            unit_text_file = open(sys.argv[3], "w")
            unit_text_string = listener.make_unit_test_string(name_of_file=sys.argv[2])
            n_two = unit_text_file.write(unit_text_string)
            unit_text_file.close()








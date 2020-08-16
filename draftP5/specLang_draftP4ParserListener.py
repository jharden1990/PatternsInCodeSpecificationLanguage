# Generated from specLang_draftP4Parser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .specLang_draftP4Parser import specLang_draftP4Parser
else:
    from specLang_draftP4Parser import specLang_draftP4Parser

# NOTES: need to have a string for the class and a method to fetch that string. This string will hold the translated code.
# NOTES: ctx.ID().getText() fetches the text for whatever ID matches in the lexer for Java; find the Python illustration
# NOTES: illustration probably in chapter 7 material

# This class defines a complete listener for a parse tree produced by specLang_draftP4Parser.
class specLang_draftP4ParserListener(ParseTreeListener):

    # Enter a parse tree produced by specLang_draftP4Parser#document.
    def enterDocument(self, ctx:specLang_draftP4Parser.DocumentContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#document.
    def exitDocument(self, ctx:specLang_draftP4Parser.DocumentContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#statement.
    def enterStatement(self, ctx:specLang_draftP4Parser.StatementContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#statement.
    def exitStatement(self, ctx:specLang_draftP4Parser.StatementContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#comment.
    def enterComment(self, ctx:specLang_draftP4Parser.CommentContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#comment.
    def exitComment(self, ctx:specLang_draftP4Parser.CommentContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#beginpart.
    def enterBeginpart(self, ctx:specLang_draftP4Parser.BeginpartContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#beginpart.
    def exitBeginpart(self, ctx:specLang_draftP4Parser.BeginpartContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#messagespart.
    def enterMessagespart(self, ctx:specLang_draftP4Parser.MessagespartContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#messagespart.
    def exitMessagespart(self, ctx:specLang_draftP4Parser.MessagespartContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#messagepart.
    def enterMessagepart(self, ctx:specLang_draftP4Parser.MessagepartContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#messagepart.
    def exitMessagepart(self, ctx:specLang_draftP4Parser.MessagepartContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#labelpart.
    def enterLabelpart(self, ctx:specLang_draftP4Parser.LabelpartContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#labelpart.
    def exitLabelpart(self, ctx:specLang_draftP4Parser.LabelpartContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#titlepart.
    def enterTitlepart(self, ctx:specLang_draftP4Parser.TitlepartContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#titlepart.
    def exitTitlepart(self, ctx:specLang_draftP4Parser.TitlepartContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#findpart.
    def enterFindpart(self, ctx:specLang_draftP4Parser.FindpartContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#findpart.
    def exitFindpart(self, ctx:specLang_draftP4Parser.FindpartContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#findclause.
    def enterFindclause(self, ctx:specLang_draftP4Parser.FindclauseContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#findclause.
    def exitFindclause(self, ctx:specLang_draftP4Parser.FindclauseContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#whereclause.
    def enterWhereclause(self, ctx:specLang_draftP4Parser.WhereclauseContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#whereclause.
    def exitWhereclause(self, ctx:specLang_draftP4Parser.WhereclauseContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#withinclause.
    def enterWithinclause(self, ctx:specLang_draftP4Parser.WithinclauseContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#withinclause.
    def exitWithinclause(self, ctx:specLang_draftP4Parser.WithinclauseContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#ifclause.
    def enterIfclause(self, ctx:specLang_draftP4Parser.IfclauseContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#ifclause.
    def exitIfclause(self, ctx:specLang_draftP4Parser.IfclauseContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#elsepart.
    def enterElsepart(self, ctx:specLang_draftP4Parser.ElsepartContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#elsepart.
    def exitElsepart(self, ctx:specLang_draftP4Parser.ElsepartContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#feedbackpart.
    def enterFeedbackpart(self, ctx:specLang_draftP4Parser.FeedbackpartContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#feedbackpart.
    def exitFeedbackpart(self, ctx:specLang_draftP4Parser.FeedbackpartContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#feedbackparenspart.
    def enterFeedbackparenspart(self, ctx:specLang_draftP4Parser.FeedbackparenspartContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#feedbackparenspart.
    def exitFeedbackparenspart(self, ctx:specLang_draftP4Parser.FeedbackparenspartContext):
        pass


    # Enter a parse tree produced by specLang_draftP4Parser#endpart.
    def enterEndpart(self, ctx:specLang_draftP4Parser.EndpartContext):
        pass

    # Exit a parse tree produced by specLang_draftP4Parser#endpart.
    def exitEndpart(self, ctx:specLang_draftP4Parser.EndpartContext):
        pass



del specLang_draftP4Parser
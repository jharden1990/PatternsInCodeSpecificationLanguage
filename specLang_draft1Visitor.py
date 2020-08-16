# Generated from specLang_draft1.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .specLang_draft1Parser import specLang_draft1Parser
else:
    from specLang_draft1Parser import specLang_draft1Parser

# This class defines a complete generic visitor for a parse tree produced by specLang_draft1Parser.

class specLang_draft1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by specLang_draft1Parser#document.
    def visitDocument(self, ctx:specLang_draft1Parser.DocumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by specLang_draft1Parser#statement.
    def visitStatement(self, ctx:specLang_draft1Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by specLang_draft1Parser#comment.
    def visitComment(self, ctx:specLang_draft1Parser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by specLang_draft1Parser#beginpart.
    def visitBeginpart(self, ctx:specLang_draft1Parser.BeginpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by specLang_draft1Parser#parameterpart.
    def visitParameterpart(self, ctx:specLang_draft1Parser.ParameterpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by specLang_draft1Parser#messagespart.
    def visitMessagespart(self, ctx:specLang_draft1Parser.MessagespartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by specLang_draft1Parser#messagepart.
    def visitMessagepart(self, ctx:specLang_draft1Parser.MessagepartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by specLang_draft1Parser#labelpart.
    def visitLabelpart(self, ctx:specLang_draft1Parser.LabelpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by specLang_draft1Parser#titlepart.
    def visitTitlepart(self, ctx:specLang_draft1Parser.TitlepartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by specLang_draft1Parser#findpart.
    def visitFindpart(self, ctx:specLang_draft1Parser.FindpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by specLang_draft1Parser#wherepart.
    def visitWherepart(self, ctx:specLang_draft1Parser.WherepartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by specLang_draft1Parser#withinpart.
    def visitWithinpart(self, ctx:specLang_draft1Parser.WithinpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by specLang_draft1Parser#ifpart.
    def visitIfpart(self, ctx:specLang_draft1Parser.IfpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by specLang_draft1Parser#feedbackpart.
    def visitFeedbackpart(self, ctx:specLang_draft1Parser.FeedbackpartContext):
        return self.visitChildren(ctx)



del specLang_draft1Parser
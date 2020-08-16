# Generated from specLang_draftP4Parser.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3$")
        buf.write("\u00b3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\6\2")
        buf.write("&\n\2\r\2\16\2\'\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\62")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5<\n\5\3\5\3\5")
        buf.write("\7\5@\n\5\f\5\16\5C\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\6\n_\n\n\r\n\16\n`\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\5\16v\n\16\3\16\3\16\3\16\5\16{\n\16\3")
        buf.write("\17\3\17\3\17\3\20\3\20\5\20\u0082\n\20\3\20\3\20\3\20")
        buf.write("\5\20\u0087\n\20\3\20\5\20\u008a\n\20\3\20\3\20\3\20\5")
        buf.write("\20\u008f\n\20\3\21\3\21\3\21\3\21\5\21\u0095\n\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u009c\n\21\7\21\u009e\n\21\f")
        buf.write("\21\16\21\u00a1\13\21\3\22\3\22\3\22\3\22\3\22\5\22\u00a8")
        buf.write("\n\22\3\22\3\22\3\22\3\22\3\22\5\22\u00af\n\22\5\22\u00b1")
        buf.write("\n\22\3\22\2\2\23\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"\2\2\2\u00b6\2%\3\2\2\2\4\61\3\2\2\2\6\63\3\2\2")
        buf.write("\2\b\67\3\2\2\2\nF\3\2\2\2\fJ\3\2\2\2\16O\3\2\2\2\20T")
        buf.write("\3\2\2\2\22Y\3\2\2\2\24b\3\2\2\2\26g\3\2\2\2\30l\3\2\2")
        buf.write("\2\32s\3\2\2\2\34|\3\2\2\2\36\u008e\3\2\2\2 \u0094\3\2")
        buf.write("\2\2\"\u00a2\3\2\2\2$&\5\4\3\2%$\3\2\2\2&\'\3\2\2\2\'")
        buf.write("%\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\7\2\2\3*\3\3\2\2\2+,")
        buf.write("\5\b\5\2,-\5\n\6\2-.\5\22\n\2./\5\"\22\2/\62\3\2\2\2\60")
        buf.write("\62\5\6\4\2\61+\3\2\2\2\61\60\3\2\2\2\62\5\3\2\2\2\63")
        buf.write("\64\7\3\2\2\64\65\7\37\2\2\65\66\7\36\2\2\66\7\3\2\2\2")
        buf.write("\678\7\7\2\289\7\33\2\29;\7\5\2\2:<\7#\2\2;:\3\2\2\2;")
        buf.write("<\3\2\2\2<A\3\2\2\2=>\7\"\2\2>@\7#\2\2?=\3\2\2\2@C\3\2")
        buf.write("\2\2A?\3\2\2\2AB\3\2\2\2BD\3\2\2\2CA\3\2\2\2DE\7 \2\2")
        buf.write("E\t\3\2\2\2FG\5\f\7\2GH\5\16\b\2HI\5\20\t\2I\13\3\2\2")
        buf.write("\2JK\7\b\2\2KL\7\4\2\2LM\7\35\2\2MN\7\34\2\2N\r\3\2\2")
        buf.write("\2OP\7\t\2\2PQ\7\4\2\2QR\7\35\2\2RS\7\34\2\2S\17\3\2\2")
        buf.write("\2TU\7\n\2\2UV\7\4\2\2VW\7\35\2\2WX\7\34\2\2X\21\3\2\2")
        buf.write("\2Y^\5\24\13\2Z_\5\26\f\2[_\5\30\r\2\\_\5\32\16\2]_\5")
        buf.write("\24\13\2^Z\3\2\2\2^[\3\2\2\2^\\\3\2\2\2^]\3\2\2\2_`\3")
        buf.write("\2\2\2`^\3\2\2\2`a\3\2\2\2a\23\3\2\2\2bc\7\13\2\2cd\7")
        buf.write("\4\2\2de\7\35\2\2ef\7\34\2\2f\25\3\2\2\2gh\7\f\2\2hi\7")
        buf.write("\4\2\2ij\7\35\2\2jk\7\34\2\2k\27\3\2\2\2lm\7\r\2\2mn\7")
        buf.write("\16\2\2no\7\13\2\2op\7\4\2\2pq\7\35\2\2qr\7\34\2\2r\31")
        buf.write("\3\2\2\2su\7\17\2\2tv\7\20\2\2ut\3\2\2\2uv\3\2\2\2vw\3")
        buf.write("\2\2\2wx\7\21\2\2xz\5\36\20\2y{\5\34\17\2zy\3\2\2\2z{")
        buf.write("\3\2\2\2{\33\3\2\2\2|}\7\27\2\2}~\5\36\20\2~\35\3\2\2")
        buf.write("\2\177\u0081\7\23\2\2\u0080\u0082\7\22\2\2\u0081\u0080")
        buf.write("\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\u0089\7\25\2\2\u0084\u0086\7\5\2\2\u0085\u0087\5 \21")
        buf.write("\2\u0086\u0085\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088")
        buf.write("\3\2\2\2\u0088\u008a\7 \2\2\u0089\u0084\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u008a\u008f\3\2\2\2\u008b\u008c\7\23\2")
        buf.write("\2\u008c\u008d\7\24\2\2\u008d\u008f\7\25\2\2\u008e\177")
        buf.write("\3\2\2\2\u008e\u008b\3\2\2\2\u008f\37\3\2\2\2\u0090\u0091")
        buf.write("\7!\2\2\u0091\u0092\7\35\2\2\u0092\u0095\7\34\2\2\u0093")
        buf.write("\u0095\7#\2\2\u0094\u0090\3\2\2\2\u0094\u0093\3\2\2\2")
        buf.write("\u0095\u009f\3\2\2\2\u0096\u009b\7\"\2\2\u0097\u0098\7")
        buf.write("!\2\2\u0098\u0099\7\35\2\2\u0099\u009c\7\34\2\2\u009a")
        buf.write("\u009c\7#\2\2\u009b\u0097\3\2\2\2\u009b\u009a\3\2\2\2")
        buf.write("\u009c\u009e\3\2\2\2\u009d\u0096\3\2\2\2\u009e\u00a1\3")
        buf.write("\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0!")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00b0\7\26\2\2\u00a3")
        buf.write("\u00a4\7\30\2\2\u00a4\u00b1\7\25\2\2\u00a5\u00a7\7\31")
        buf.write("\2\2\u00a6\u00a8\7\22\2\2\u00a7\u00a6\3\2\2\2\u00a7\u00a8")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ae\7\25\2\2\u00aa")
        buf.write("\u00ab\7\5\2\2\u00ab\u00ac\5 \21\2\u00ac\u00ad\7 \2\2")
        buf.write("\u00ad\u00af\3\2\2\2\u00ae\u00aa\3\2\2\2\u00ae\u00af\3")
        buf.write("\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00a3\3\2\2\2\u00b0\u00a5")
        buf.write("\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1#\3\2\2\2\24\'\61;A")
        buf.write("^`uz\u0081\u0086\u0089\u008e\u0094\u009b\u009f\u00a7\u00ae")
        buf.write("\u00b0")
        return buf.getvalue()


class specLang_draftP4Parser ( Parser ):

    grammarFileName = "specLang_draftP4Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "<INVALID>", 
                     "'BEGIN'", "'MESSAGE'", "'LABEL'", "'TITLE'", "'FIND'", 
                     "'WHERE'", "'WITHIN'", "<INVALID>", "'IF'", "'NOT'", 
                     "'FOUND'", "'GENTLE'", "'GIVE'", "'NO'", "'FEEDBACK'", 
                     "'END'", "'ELSE'", "'WITHOUT'", "'WITH'", "'AS'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "')'", "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "OPEN_COMMENT", "OPEN_CODE", "OPEN_PARENS", 
                      "WHITESPACE", "BEGIN", "MESSAGE", "LABEL", "TITLE", 
                      "FIND", "WHERE", "WITHIN", "EXPRESSION", "IF", "NOT", 
                      "FOUND", "GENTLE", "GIVE", "NO", "FEEDBACK", "END", 
                      "ELSE", "WITHOUT", "WITH", "AS", "NAME", "CLOSE_CODE", 
                      "CODE_TEXT", "CLOSE_COMMENT", "COMMENT_TEXT", "CLOSE_PARENS", 
                      "OPEN_CODE_IN_PARENS", "COMMA", "PARENS_TEXT", "WHITESPACE_PARENS" ]

    RULE_document = 0
    RULE_statement = 1
    RULE_comment = 2
    RULE_beginpart = 3
    RULE_messagespart = 4
    RULE_messagepart = 5
    RULE_labelpart = 6
    RULE_titlepart = 7
    RULE_findpart = 8
    RULE_findclause = 9
    RULE_whereclause = 10
    RULE_withinclause = 11
    RULE_ifclause = 12
    RULE_elsepart = 13
    RULE_feedbackpart = 14
    RULE_feedbackparenspart = 15
    RULE_endpart = 16

    ruleNames =  [ "document", "statement", "comment", "beginpart", "messagespart", 
                   "messagepart", "labelpart", "titlepart", "findpart", 
                   "findclause", "whereclause", "withinclause", "ifclause", 
                   "elsepart", "feedbackpart", "feedbackparenspart", "endpart" ]

    EOF = Token.EOF
    OPEN_COMMENT=1
    OPEN_CODE=2
    OPEN_PARENS=3
    WHITESPACE=4
    BEGIN=5
    MESSAGE=6
    LABEL=7
    TITLE=8
    FIND=9
    WHERE=10
    WITHIN=11
    EXPRESSION=12
    IF=13
    NOT=14
    FOUND=15
    GENTLE=16
    GIVE=17
    NO=18
    FEEDBACK=19
    END=20
    ELSE=21
    WITHOUT=22
    WITH=23
    AS=24
    NAME=25
    CLOSE_CODE=26
    CODE_TEXT=27
    CLOSE_COMMENT=28
    COMMENT_TEXT=29
    CLOSE_PARENS=30
    OPEN_CODE_IN_PARENS=31
    COMMA=32
    PARENS_TEXT=33
    WHITESPACE_PARENS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(specLang_draftP4Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(specLang_draftP4Parser.StatementContext)
            else:
                return self.getTypedRuleContext(specLang_draftP4Parser.StatementContext,i)


        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)




    def document(self):

        localctx = specLang_draftP4Parser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.statement()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==specLang_draftP4Parser.OPEN_COMMENT or _la==specLang_draftP4Parser.BEGIN):
                    break

            self.state = 39
            self.match(specLang_draftP4Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def beginpart(self):
            return self.getTypedRuleContext(specLang_draftP4Parser.BeginpartContext,0)


        def messagespart(self):
            return self.getTypedRuleContext(specLang_draftP4Parser.MessagespartContext,0)


        def findpart(self):
            return self.getTypedRuleContext(specLang_draftP4Parser.FindpartContext,0)


        def endpart(self):
            return self.getTypedRuleContext(specLang_draftP4Parser.EndpartContext,0)


        def comment(self):
            return self.getTypedRuleContext(specLang_draftP4Parser.CommentContext,0)


        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = specLang_draftP4Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [specLang_draftP4Parser.BEGIN]:
                self.state = 41
                self.beginpart()
                self.state = 42
                self.messagespart()
                self.state = 43
                self.findpart()
                self.state = 44
                self.endpart()
                pass
            elif token in [specLang_draftP4Parser.OPEN_COMMENT]:
                self.state = 46
                self.comment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_COMMENT(self):
            return self.getToken(specLang_draftP4Parser.OPEN_COMMENT, 0)

        def COMMENT_TEXT(self):
            return self.getToken(specLang_draftP4Parser.COMMENT_TEXT, 0)

        def CLOSE_COMMENT(self):
            return self.getToken(specLang_draftP4Parser.CLOSE_COMMENT, 0)

        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = specLang_draftP4Parser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(specLang_draftP4Parser.OPEN_COMMENT)
            self.state = 50
            self.match(specLang_draftP4Parser.COMMENT_TEXT)
            self.state = 51
            self.match(specLang_draftP4Parser.CLOSE_COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BeginpartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(specLang_draftP4Parser.BEGIN, 0)

        def NAME(self):
            return self.getToken(specLang_draftP4Parser.NAME, 0)

        def OPEN_PARENS(self):
            return self.getToken(specLang_draftP4Parser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(specLang_draftP4Parser.CLOSE_PARENS, 0)

        def PARENS_TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(specLang_draftP4Parser.PARENS_TEXT)
            else:
                return self.getToken(specLang_draftP4Parser.PARENS_TEXT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(specLang_draftP4Parser.COMMA)
            else:
                return self.getToken(specLang_draftP4Parser.COMMA, i)

        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_beginpart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBeginpart" ):
                listener.enterBeginpart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBeginpart" ):
                listener.exitBeginpart(self)




    def beginpart(self):

        localctx = specLang_draftP4Parser.BeginpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_beginpart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(specLang_draftP4Parser.BEGIN)
            self.state = 54
            self.match(specLang_draftP4Parser.NAME)
            self.state = 55
            self.match(specLang_draftP4Parser.OPEN_PARENS)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==specLang_draftP4Parser.PARENS_TEXT:
                self.state = 56
                self.match(specLang_draftP4Parser.PARENS_TEXT)


            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==specLang_draftP4Parser.COMMA:
                self.state = 59
                self.match(specLang_draftP4Parser.COMMA)
                self.state = 60
                self.match(specLang_draftP4Parser.PARENS_TEXT)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(specLang_draftP4Parser.CLOSE_PARENS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MessagespartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def messagepart(self):
            return self.getTypedRuleContext(specLang_draftP4Parser.MessagepartContext,0)


        def labelpart(self):
            return self.getTypedRuleContext(specLang_draftP4Parser.LabelpartContext,0)


        def titlepart(self):
            return self.getTypedRuleContext(specLang_draftP4Parser.TitlepartContext,0)


        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_messagespart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMessagespart" ):
                listener.enterMessagespart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMessagespart" ):
                listener.exitMessagespart(self)




    def messagespart(self):

        localctx = specLang_draftP4Parser.MessagespartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_messagespart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.messagepart()
            self.state = 69
            self.labelpart()
            self.state = 70
            self.titlepart()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MessagepartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MESSAGE(self):
            return self.getToken(specLang_draftP4Parser.MESSAGE, 0)

        def OPEN_CODE(self):
            return self.getToken(specLang_draftP4Parser.OPEN_CODE, 0)

        def CODE_TEXT(self):
            return self.getToken(specLang_draftP4Parser.CODE_TEXT, 0)

        def CLOSE_CODE(self):
            return self.getToken(specLang_draftP4Parser.CLOSE_CODE, 0)

        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_messagepart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMessagepart" ):
                listener.enterMessagepart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMessagepart" ):
                listener.exitMessagepart(self)




    def messagepart(self):

        localctx = specLang_draftP4Parser.MessagepartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_messagepart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(specLang_draftP4Parser.MESSAGE)
            self.state = 73
            self.match(specLang_draftP4Parser.OPEN_CODE)
            self.state = 74
            self.match(specLang_draftP4Parser.CODE_TEXT)
            self.state = 75
            self.match(specLang_draftP4Parser.CLOSE_CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelpartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABEL(self):
            return self.getToken(specLang_draftP4Parser.LABEL, 0)

        def OPEN_CODE(self):
            return self.getToken(specLang_draftP4Parser.OPEN_CODE, 0)

        def CODE_TEXT(self):
            return self.getToken(specLang_draftP4Parser.CODE_TEXT, 0)

        def CLOSE_CODE(self):
            return self.getToken(specLang_draftP4Parser.CLOSE_CODE, 0)

        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_labelpart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelpart" ):
                listener.enterLabelpart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelpart" ):
                listener.exitLabelpart(self)




    def labelpart(self):

        localctx = specLang_draftP4Parser.LabelpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_labelpart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(specLang_draftP4Parser.LABEL)
            self.state = 78
            self.match(specLang_draftP4Parser.OPEN_CODE)
            self.state = 79
            self.match(specLang_draftP4Parser.CODE_TEXT)
            self.state = 80
            self.match(specLang_draftP4Parser.CLOSE_CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TitlepartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TITLE(self):
            return self.getToken(specLang_draftP4Parser.TITLE, 0)

        def OPEN_CODE(self):
            return self.getToken(specLang_draftP4Parser.OPEN_CODE, 0)

        def CODE_TEXT(self):
            return self.getToken(specLang_draftP4Parser.CODE_TEXT, 0)

        def CLOSE_CODE(self):
            return self.getToken(specLang_draftP4Parser.CLOSE_CODE, 0)

        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_titlepart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTitlepart" ):
                listener.enterTitlepart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTitlepart" ):
                listener.exitTitlepart(self)




    def titlepart(self):

        localctx = specLang_draftP4Parser.TitlepartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_titlepart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(specLang_draftP4Parser.TITLE)
            self.state = 83
            self.match(specLang_draftP4Parser.OPEN_CODE)
            self.state = 84
            self.match(specLang_draftP4Parser.CODE_TEXT)
            self.state = 85
            self.match(specLang_draftP4Parser.CLOSE_CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FindpartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def findclause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(specLang_draftP4Parser.FindclauseContext)
            else:
                return self.getTypedRuleContext(specLang_draftP4Parser.FindclauseContext,i)


        def whereclause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(specLang_draftP4Parser.WhereclauseContext)
            else:
                return self.getTypedRuleContext(specLang_draftP4Parser.WhereclauseContext,i)


        def withinclause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(specLang_draftP4Parser.WithinclauseContext)
            else:
                return self.getTypedRuleContext(specLang_draftP4Parser.WithinclauseContext,i)


        def ifclause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(specLang_draftP4Parser.IfclauseContext)
            else:
                return self.getTypedRuleContext(specLang_draftP4Parser.IfclauseContext,i)


        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_findpart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFindpart" ):
                listener.enterFindpart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFindpart" ):
                listener.exitFindpart(self)




    def findpart(self):

        localctx = specLang_draftP4Parser.FindpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_findpart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.findclause()
            self.state = 92 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 92
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [specLang_draftP4Parser.WHERE]:
                    self.state = 88
                    self.whereclause()
                    pass
                elif token in [specLang_draftP4Parser.WITHIN]:
                    self.state = 89
                    self.withinclause()
                    pass
                elif token in [specLang_draftP4Parser.IF]:
                    self.state = 90
                    self.ifclause()
                    pass
                elif token in [specLang_draftP4Parser.FIND]:
                    self.state = 91
                    self.findclause()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 94 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << specLang_draftP4Parser.FIND) | (1 << specLang_draftP4Parser.WHERE) | (1 << specLang_draftP4Parser.WITHIN) | (1 << specLang_draftP4Parser.IF))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FindclauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIND(self):
            return self.getToken(specLang_draftP4Parser.FIND, 0)

        def OPEN_CODE(self):
            return self.getToken(specLang_draftP4Parser.OPEN_CODE, 0)

        def CODE_TEXT(self):
            return self.getToken(specLang_draftP4Parser.CODE_TEXT, 0)

        def CLOSE_CODE(self):
            return self.getToken(specLang_draftP4Parser.CLOSE_CODE, 0)

        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_findclause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFindclause" ):
                listener.enterFindclause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFindclause" ):
                listener.exitFindclause(self)




    def findclause(self):

        localctx = specLang_draftP4Parser.FindclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_findclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(specLang_draftP4Parser.FIND)
            self.state = 97
            self.match(specLang_draftP4Parser.OPEN_CODE)
            self.state = 98
            self.match(specLang_draftP4Parser.CODE_TEXT)
            self.state = 99
            self.match(specLang_draftP4Parser.CLOSE_CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereclauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(specLang_draftP4Parser.WHERE, 0)

        def OPEN_CODE(self):
            return self.getToken(specLang_draftP4Parser.OPEN_CODE, 0)

        def CODE_TEXT(self):
            return self.getToken(specLang_draftP4Parser.CODE_TEXT, 0)

        def CLOSE_CODE(self):
            return self.getToken(specLang_draftP4Parser.CLOSE_CODE, 0)

        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_whereclause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereclause" ):
                listener.enterWhereclause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereclause" ):
                listener.exitWhereclause(self)




    def whereclause(self):

        localctx = specLang_draftP4Parser.WhereclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whereclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(specLang_draftP4Parser.WHERE)
            self.state = 102
            self.match(specLang_draftP4Parser.OPEN_CODE)
            self.state = 103
            self.match(specLang_draftP4Parser.CODE_TEXT)
            self.state = 104
            self.match(specLang_draftP4Parser.CLOSE_CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithinclauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITHIN(self):
            return self.getToken(specLang_draftP4Parser.WITHIN, 0)

        def EXPRESSION(self):
            return self.getToken(specLang_draftP4Parser.EXPRESSION, 0)

        def FIND(self):
            return self.getToken(specLang_draftP4Parser.FIND, 0)

        def OPEN_CODE(self):
            return self.getToken(specLang_draftP4Parser.OPEN_CODE, 0)

        def CODE_TEXT(self):
            return self.getToken(specLang_draftP4Parser.CODE_TEXT, 0)

        def CLOSE_CODE(self):
            return self.getToken(specLang_draftP4Parser.CLOSE_CODE, 0)

        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_withinclause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWithinclause" ):
                listener.enterWithinclause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWithinclause" ):
                listener.exitWithinclause(self)




    def withinclause(self):

        localctx = specLang_draftP4Parser.WithinclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_withinclause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(specLang_draftP4Parser.WITHIN)
            self.state = 107
            self.match(specLang_draftP4Parser.EXPRESSION)
            self.state = 108
            self.match(specLang_draftP4Parser.FIND)
            self.state = 109
            self.match(specLang_draftP4Parser.OPEN_CODE)
            self.state = 110
            self.match(specLang_draftP4Parser.CODE_TEXT)
            self.state = 111
            self.match(specLang_draftP4Parser.CLOSE_CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfclauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(specLang_draftP4Parser.IF, 0)

        def FOUND(self):
            return self.getToken(specLang_draftP4Parser.FOUND, 0)

        def feedbackpart(self):
            return self.getTypedRuleContext(specLang_draftP4Parser.FeedbackpartContext,0)


        def NOT(self):
            return self.getToken(specLang_draftP4Parser.NOT, 0)

        def elsepart(self):
            return self.getTypedRuleContext(specLang_draftP4Parser.ElsepartContext,0)


        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_ifclause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfclause" ):
                listener.enterIfclause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfclause" ):
                listener.exitIfclause(self)




    def ifclause(self):

        localctx = specLang_draftP4Parser.IfclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifclause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(specLang_draftP4Parser.IF)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==specLang_draftP4Parser.NOT:
                self.state = 114
                self.match(specLang_draftP4Parser.NOT)


            self.state = 117
            self.match(specLang_draftP4Parser.FOUND)
            self.state = 118
            self.feedbackpart()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==specLang_draftP4Parser.ELSE:
                self.state = 119
                self.elsepart()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsepartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(specLang_draftP4Parser.ELSE, 0)

        def feedbackpart(self):
            return self.getTypedRuleContext(specLang_draftP4Parser.FeedbackpartContext,0)


        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_elsepart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElsepart" ):
                listener.enterElsepart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElsepart" ):
                listener.exitElsepart(self)




    def elsepart(self):

        localctx = specLang_draftP4Parser.ElsepartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_elsepart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(specLang_draftP4Parser.ELSE)
            self.state = 123
            self.feedbackpart()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeedbackpartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GIVE(self):
            return self.getToken(specLang_draftP4Parser.GIVE, 0)

        def FEEDBACK(self):
            return self.getToken(specLang_draftP4Parser.FEEDBACK, 0)

        def NO(self):
            return self.getToken(specLang_draftP4Parser.NO, 0)

        def GENTLE(self):
            return self.getToken(specLang_draftP4Parser.GENTLE, 0)

        def OPEN_PARENS(self):
            return self.getToken(specLang_draftP4Parser.OPEN_PARENS, 0)

        def CLOSE_PARENS(self):
            return self.getToken(specLang_draftP4Parser.CLOSE_PARENS, 0)

        def feedbackparenspart(self):
            return self.getTypedRuleContext(specLang_draftP4Parser.FeedbackparenspartContext,0)


        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_feedbackpart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeedbackpart" ):
                listener.enterFeedbackpart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeedbackpart" ):
                listener.exitFeedbackpart(self)




    def feedbackpart(self):

        localctx = specLang_draftP4Parser.FeedbackpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_feedbackpart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 125
                self.match(specLang_draftP4Parser.GIVE)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==specLang_draftP4Parser.GENTLE:
                    self.state = 126
                    self.match(specLang_draftP4Parser.GENTLE)


                self.state = 129
                self.match(specLang_draftP4Parser.FEEDBACK)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==specLang_draftP4Parser.OPEN_PARENS:
                    self.state = 130
                    self.match(specLang_draftP4Parser.OPEN_PARENS)
                    self.state = 132
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==specLang_draftP4Parser.OPEN_CODE_IN_PARENS or _la==specLang_draftP4Parser.PARENS_TEXT:
                        self.state = 131
                        self.feedbackparenspart()


                    self.state = 134
                    self.match(specLang_draftP4Parser.CLOSE_PARENS)


                pass

            elif la_ == 2:
                self.state = 137
                self.match(specLang_draftP4Parser.GIVE)
                self.state = 138
                self.match(specLang_draftP4Parser.NO)
                self.state = 139
                self.match(specLang_draftP4Parser.FEEDBACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FeedbackparenspartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_CODE_IN_PARENS(self, i:int=None):
            if i is None:
                return self.getTokens(specLang_draftP4Parser.OPEN_CODE_IN_PARENS)
            else:
                return self.getToken(specLang_draftP4Parser.OPEN_CODE_IN_PARENS, i)

        def CODE_TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(specLang_draftP4Parser.CODE_TEXT)
            else:
                return self.getToken(specLang_draftP4Parser.CODE_TEXT, i)

        def CLOSE_CODE(self, i:int=None):
            if i is None:
                return self.getTokens(specLang_draftP4Parser.CLOSE_CODE)
            else:
                return self.getToken(specLang_draftP4Parser.CLOSE_CODE, i)

        def PARENS_TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(specLang_draftP4Parser.PARENS_TEXT)
            else:
                return self.getToken(specLang_draftP4Parser.PARENS_TEXT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(specLang_draftP4Parser.COMMA)
            else:
                return self.getToken(specLang_draftP4Parser.COMMA, i)

        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_feedbackparenspart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeedbackparenspart" ):
                listener.enterFeedbackparenspart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeedbackparenspart" ):
                listener.exitFeedbackparenspart(self)




    def feedbackparenspart(self):

        localctx = specLang_draftP4Parser.FeedbackparenspartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_feedbackparenspart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [specLang_draftP4Parser.OPEN_CODE_IN_PARENS]:
                self.state = 142
                self.match(specLang_draftP4Parser.OPEN_CODE_IN_PARENS)
                self.state = 143
                self.match(specLang_draftP4Parser.CODE_TEXT)
                self.state = 144
                self.match(specLang_draftP4Parser.CLOSE_CODE)
                pass
            elif token in [specLang_draftP4Parser.PARENS_TEXT]:
                self.state = 145
                self.match(specLang_draftP4Parser.PARENS_TEXT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==specLang_draftP4Parser.COMMA:
                self.state = 148
                self.match(specLang_draftP4Parser.COMMA)
                self.state = 153
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [specLang_draftP4Parser.OPEN_CODE_IN_PARENS]:
                    self.state = 149
                    self.match(specLang_draftP4Parser.OPEN_CODE_IN_PARENS)
                    self.state = 150
                    self.match(specLang_draftP4Parser.CODE_TEXT)
                    self.state = 151
                    self.match(specLang_draftP4Parser.CLOSE_CODE)
                    pass
                elif token in [specLang_draftP4Parser.PARENS_TEXT]:
                    self.state = 152
                    self.match(specLang_draftP4Parser.PARENS_TEXT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndpartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(specLang_draftP4Parser.END, 0)

        def WITHOUT(self):
            return self.getToken(specLang_draftP4Parser.WITHOUT, 0)

        def FEEDBACK(self):
            return self.getToken(specLang_draftP4Parser.FEEDBACK, 0)

        def WITH(self):
            return self.getToken(specLang_draftP4Parser.WITH, 0)

        def GENTLE(self):
            return self.getToken(specLang_draftP4Parser.GENTLE, 0)

        def OPEN_PARENS(self):
            return self.getToken(specLang_draftP4Parser.OPEN_PARENS, 0)

        def feedbackparenspart(self):
            return self.getTypedRuleContext(specLang_draftP4Parser.FeedbackparenspartContext,0)


        def CLOSE_PARENS(self):
            return self.getToken(specLang_draftP4Parser.CLOSE_PARENS, 0)

        def getRuleIndex(self):
            return specLang_draftP4Parser.RULE_endpart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndpart" ):
                listener.enterEndpart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndpart" ):
                listener.exitEndpart(self)




    def endpart(self):

        localctx = specLang_draftP4Parser.EndpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_endpart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(specLang_draftP4Parser.END)
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [specLang_draftP4Parser.WITHOUT]:
                self.state = 161
                self.match(specLang_draftP4Parser.WITHOUT)
                self.state = 162
                self.match(specLang_draftP4Parser.FEEDBACK)
                pass
            elif token in [specLang_draftP4Parser.WITH]:
                self.state = 163
                self.match(specLang_draftP4Parser.WITH)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==specLang_draftP4Parser.GENTLE:
                    self.state = 164
                    self.match(specLang_draftP4Parser.GENTLE)


                self.state = 167
                self.match(specLang_draftP4Parser.FEEDBACK)
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==specLang_draftP4Parser.OPEN_PARENS:
                    self.state = 168
                    self.match(specLang_draftP4Parser.OPEN_PARENS)
                    self.state = 169
                    self.feedbackparenspart()
                    self.state = 170
                    self.match(specLang_draftP4Parser.CLOSE_PARENS)


                pass
            elif token in [specLang_draftP4Parser.EOF, specLang_draftP4Parser.OPEN_COMMENT, specLang_draftP4Parser.BEGIN]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






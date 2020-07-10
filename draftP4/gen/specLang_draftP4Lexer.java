// Generated from C:/Users/jhard/Desktop/School_Stuff/Work Stuff/VT GRA 2019-20 WORK/specLang_work/grammar_testing/separate lexer and parser/Python Versions/draftP4\specLang_draftP4Lexer.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class specLang_draftP4Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		OPEN_COMMENT=1, OPEN_CODE=2, OPEN_PARENS=3, WHITESPACE=4, BEGIN=5, MESSAGE=6, 
		LABEL=7, TITLE=8, FIND=9, WHERE=10, WITHIN=11, EXPRESSION=12, IF=13, NOT=14, 
		FOUND=15, GENTLE=16, GIVE=17, NO=18, FEEDBACK=19, END=20, ELSE=21, WITHOUT=22, 
		WITH=23, AS=24, NAME=25, CLOSE_CODE=26, CODE_TEXT=27, CLOSE_COMMENT=28, 
		COMMENT_TEXT=29, CLOSE_PARENS=30, OPEN_CODE_IN_PARENS=31, COMMA=32, PARENS_TEXT=33, 
		WHITESPACE_PARENS=34;
	public static final int
		CODE=1, COMMENT=2, PARENS=3;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE", "CODE", "COMMENT", "PARENS"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"OPEN_COMMENT", "OPEN_CODE", "OPEN_PARENS", "WHITESPACE", "BEGIN", "MESSAGE", 
			"LABEL", "TITLE", "FIND", "WHERE", "WITHIN", "EXPRESSION", "IF", "NOT", 
			"FOUND", "GENTLE", "GIVE", "NO", "FEEDBACK", "END", "ELSE", "WITHOUT", 
			"WITH", "AS", "NAME", "CLOSE_CODE", "CODE_TEXT", "CLOSE_COMMENT", "COMMENT_TEXT", 
			"CLOSE_PARENS", "OPEN_CODE_IN_PARENS", "COMMA", "PARENS_TEXT", "WHITESPACE_PARENS", 
			"LOWERCASE", "UPPERCASE", "DIGIT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'('", null, "'BEGIN'", "'MESSAGE'", "'LABEL'", "'TITLE'", 
			"'FIND'", "'WHERE'", "'WITHIN'", null, "'IF'", "'NOT'", "'FOUND'", "'GENTLE'", 
			"'GIVE'", "'NO'", "'FEEDBACK'", "'END'", "'ELSE'", "'WITHOUT'", "'WITH'", 
			"'AS'", null, null, null, null, null, "')'", null, "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "OPEN_COMMENT", "OPEN_CODE", "OPEN_PARENS", "WHITESPACE", "BEGIN", 
			"MESSAGE", "LABEL", "TITLE", "FIND", "WHERE", "WITHIN", "EXPRESSION", 
			"IF", "NOT", "FOUND", "GENTLE", "GIVE", "NO", "FEEDBACK", "END", "ELSE", 
			"WITHOUT", "WITH", "AS", "NAME", "CLOSE_CODE", "CODE_TEXT", "CLOSE_COMMENT", 
			"COMMENT_TEXT", "CLOSE_PARENS", "OPEN_CODE_IN_PARENS", "COMMA", "PARENS_TEXT", 
			"WHITESPACE_PARENS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public specLang_draftP4Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "specLang_draftP4Lexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2$\u0110\b\1\b\1\b"+
		"\1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t"+
		"\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21"+
		"\t\21\4\22\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30"+
		"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37"+
		"\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\3\2\3\2\3\2\3\2\3\3"+
		"\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\6\5^\n\5\r\5\16\5_\3\5\3\5\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\6\r\u0096\n"+
		"\r\r\r\16\r\u0097\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22"+
		"\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32"+
		"\3\32\3\32\6\32\u00df\n\32\r\32\16\32\u00e0\3\33\3\33\3\33\3\33\3\34\6"+
		"\34\u00e8\n\34\r\34\16\34\u00e9\3\35\3\35\3\35\3\35\3\36\6\36\u00f1\n"+
		"\36\r\36\16\36\u00f2\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3\"\6\"\u0100"+
		"\n\"\r\"\16\"\u0101\3#\6#\u0105\n#\r#\16#\u0106\3#\3#\3$\3$\3%\3%\3&\3"+
		"&\2\2\'\6\3\b\4\n\5\f\6\16\7\20\b\22\t\24\n\26\13\30\f\32\r\34\16\36\17"+
		" \20\"\21$\22&\23(\24*\25,\26.\27\60\30\62\31\64\32\66\338\34:\35<\36"+
		">\37@ B!D\"F#H$J\2L\2N\2\6\2\3\4\5\t\5\2\13\f\17\17\"\"\3\2bb\3\2%%\b"+
		"\2\13\f\17\17\"\"++..bb\3\2c|\3\2C\\\3\2\62;\2\u0115\2\6\3\2\2\2\2\b\3"+
		"\2\2\2\2\n\3\2\2\2\2\f\3\2\2\2\2\16\3\2\2\2\2\20\3\2\2\2\2\22\3\2\2\2"+
		"\2\24\3\2\2\2\2\26\3\2\2\2\2\30\3\2\2\2\2\32\3\2\2\2\2\34\3\2\2\2\2\36"+
		"\3\2\2\2\2 \3\2\2\2\2\"\3\2\2\2\2$\3\2\2\2\2&\3\2\2\2\2(\3\2\2\2\2*\3"+
		"\2\2\2\2,\3\2\2\2\2.\3\2\2\2\2\60\3\2\2\2\2\62\3\2\2\2\2\64\3\2\2\2\2"+
		"\66\3\2\2\2\38\3\2\2\2\3:\3\2\2\2\4<\3\2\2\2\4>\3\2\2\2\5@\3\2\2\2\5B"+
		"\3\2\2\2\5D\3\2\2\2\5F\3\2\2\2\5H\3\2\2\2\6P\3\2\2\2\bT\3\2\2\2\nX\3\2"+
		"\2\2\f]\3\2\2\2\16c\3\2\2\2\20i\3\2\2\2\22q\3\2\2\2\24w\3\2\2\2\26}\3"+
		"\2\2\2\30\u0082\3\2\2\2\32\u0088\3\2\2\2\34\u008f\3\2\2\2\36\u009c\3\2"+
		"\2\2 \u009f\3\2\2\2\"\u00a3\3\2\2\2$\u00a9\3\2\2\2&\u00b0\3\2\2\2(\u00b5"+
		"\3\2\2\2*\u00b8\3\2\2\2,\u00c1\3\2\2\2.\u00c5\3\2\2\2\60\u00ca\3\2\2\2"+
		"\62\u00d2\3\2\2\2\64\u00d7\3\2\2\2\66\u00de\3\2\2\28\u00e2\3\2\2\2:\u00e7"+
		"\3\2\2\2<\u00eb\3\2\2\2>\u00f0\3\2\2\2@\u00f4\3\2\2\2B\u00f8\3\2\2\2D"+
		"\u00fc\3\2\2\2F\u00ff\3\2\2\2H\u0104\3\2\2\2J\u010a\3\2\2\2L\u010c\3\2"+
		"\2\2N\u010e\3\2\2\2PQ\7%\2\2QR\3\2\2\2RS\b\2\2\2S\7\3\2\2\2TU\7b\2\2U"+
		"V\3\2\2\2VW\b\3\3\2W\t\3\2\2\2XY\7*\2\2YZ\3\2\2\2Z[\b\4\4\2[\13\3\2\2"+
		"\2\\^\t\2\2\2]\\\3\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\b\5"+
		"\5\2b\r\3\2\2\2cd\7D\2\2de\7G\2\2ef\7I\2\2fg\7K\2\2gh\7P\2\2h\17\3\2\2"+
		"\2ij\7O\2\2jk\7G\2\2kl\7U\2\2lm\7U\2\2mn\7C\2\2no\7I\2\2op\7G\2\2p\21"+
		"\3\2\2\2qr\7N\2\2rs\7C\2\2st\7D\2\2tu\7G\2\2uv\7N\2\2v\23\3\2\2\2wx\7"+
		"V\2\2xy\7K\2\2yz\7V\2\2z{\7N\2\2{|\7G\2\2|\25\3\2\2\2}~\7H\2\2~\177\7"+
		"K\2\2\177\u0080\7P\2\2\u0080\u0081\7F\2\2\u0081\27\3\2\2\2\u0082\u0083"+
		"\7Y\2\2\u0083\u0084\7J\2\2\u0084\u0085\7G\2\2\u0085\u0086\7T\2\2\u0086"+
		"\u0087\7G\2\2\u0087\31\3\2\2\2\u0088\u0089\7Y\2\2\u0089\u008a\7K\2\2\u008a"+
		"\u008b\7V\2\2\u008b\u008c\7J\2\2\u008c\u008d\7K\2\2\u008d\u008e\7P\2\2"+
		"\u008e\33\3\2\2\2\u008f\u0090\7a\2\2\u0090\u0091\7a\2\2\u0091\u0095\3"+
		"\2\2\2\u0092\u0096\5J$\2\u0093\u0096\5L%\2\u0094\u0096\5N&\2\u0095\u0092"+
		"\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097"+
		"\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\7a"+
		"\2\2\u009a\u009b\7a\2\2\u009b\35\3\2\2\2\u009c\u009d\7K\2\2\u009d\u009e"+
		"\7H\2\2\u009e\37\3\2\2\2\u009f\u00a0\7P\2\2\u00a0\u00a1\7Q\2\2\u00a1\u00a2"+
		"\7V\2\2\u00a2!\3\2\2\2\u00a3\u00a4\7H\2\2\u00a4\u00a5\7Q\2\2\u00a5\u00a6"+
		"\7W\2\2\u00a6\u00a7\7P\2\2\u00a7\u00a8\7F\2\2\u00a8#\3\2\2\2\u00a9\u00aa"+
		"\7I\2\2\u00aa\u00ab\7G\2\2\u00ab\u00ac\7P\2\2\u00ac\u00ad\7V\2\2\u00ad"+
		"\u00ae\7N\2\2\u00ae\u00af\7G\2\2\u00af%\3\2\2\2\u00b0\u00b1\7I\2\2\u00b1"+
		"\u00b2\7K\2\2\u00b2\u00b3\7X\2\2\u00b3\u00b4\7G\2\2\u00b4\'\3\2\2\2\u00b5"+
		"\u00b6\7P\2\2\u00b6\u00b7\7Q\2\2\u00b7)\3\2\2\2\u00b8\u00b9\7H\2\2\u00b9"+
		"\u00ba\7G\2\2\u00ba\u00bb\7G\2\2\u00bb\u00bc\7F\2\2\u00bc\u00bd\7D\2\2"+
		"\u00bd\u00be\7C\2\2\u00be\u00bf\7E\2\2\u00bf\u00c0\7M\2\2\u00c0+\3\2\2"+
		"\2\u00c1\u00c2\7G\2\2\u00c2\u00c3\7P\2\2\u00c3\u00c4\7F\2\2\u00c4-\3\2"+
		"\2\2\u00c5\u00c6\7G\2\2\u00c6\u00c7\7N\2\2\u00c7\u00c8\7U\2\2\u00c8\u00c9"+
		"\7G\2\2\u00c9/\3\2\2\2\u00ca\u00cb\7Y\2\2\u00cb\u00cc\7K\2\2\u00cc\u00cd"+
		"\7V\2\2\u00cd\u00ce\7J\2\2\u00ce\u00cf\7Q\2\2\u00cf\u00d0\7W\2\2\u00d0"+
		"\u00d1\7V\2\2\u00d1\61\3\2\2\2\u00d2\u00d3\7Y\2\2\u00d3\u00d4\7K\2\2\u00d4"+
		"\u00d5\7V\2\2\u00d5\u00d6\7J\2\2\u00d6\63\3\2\2\2\u00d7\u00d8\7C\2\2\u00d8"+
		"\u00d9\7U\2\2\u00d9\65\3\2\2\2\u00da\u00df\5J$\2\u00db\u00df\5L%\2\u00dc"+
		"\u00df\5N&\2\u00dd\u00df\7a\2\2\u00de\u00da\3\2\2\2\u00de\u00db\3\2\2"+
		"\2\u00de\u00dc\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00de"+
		"\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\67\3\2\2\2\u00e2\u00e3\7b\2\2\u00e3"+
		"\u00e4\3\2\2\2\u00e4\u00e5\b\33\6\2\u00e59\3\2\2\2\u00e6\u00e8\n\3\2\2"+
		"\u00e7\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea"+
		"\3\2\2\2\u00ea;\3\2\2\2\u00eb\u00ec\7%\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee"+
		"\b\35\7\2\u00ee=\3\2\2\2\u00ef\u00f1\n\4\2\2\u00f0\u00ef\3\2\2\2\u00f1"+
		"\u00f2\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3?\3\2\2\2"+
		"\u00f4\u00f5\7+\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\b\37\7\2\u00f7A\3"+
		"\2\2\2\u00f8\u00f9\7b\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\b \3\2\u00fb"+
		"C\3\2\2\2\u00fc\u00fd\7.\2\2\u00fdE\3\2\2\2\u00fe\u0100\n\5\2\2\u00ff"+
		"\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3\2"+
		"\2\2\u0102G\3\2\2\2\u0103\u0105\t\2\2\2\u0104\u0103\3\2\2\2\u0105\u0106"+
		"\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\3\2\2\2\u0108"+
		"\u0109\b#\5\2\u0109I\3\2\2\2\u010a\u010b\t\6\2\2\u010bK\3\2\2\2\u010c"+
		"\u010d\t\7\2\2\u010dM\3\2\2\2\u010e\u010f\t\b\2\2\u010fO\3\2\2\2\17\2"+
		"\3\4\5_\u0095\u0097\u00de\u00e0\u00e9\u00f2\u0101\u0106\b\4\4\2\7\3\2"+
		"\4\5\2\b\2\2\6\2\2\4\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
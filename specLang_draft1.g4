grammar specLang_draft1;

/*
 * Parser rules
 */

document				: WHITESPACE* (statement WHITESPACE+)+ EOF;
statement				: (beginpart WHITESPACE* messagespart WHITESPACE* findpart WHITESPACE* END | comment);
comment 				: '#' WORDS_NO_HASH '#';
beginpart 				: BEGIN WHITESPACE+ WORD '(' parameterpart ')';
parameterpart 			: WORD (WHITESPACE* COMMA WHITESPACE* WORD)*;
messagespart 			: messagepart WHITESPACE+ labelpart WHITESPACE+ titlepart;
messagepart 			: MESSAGE WHITESPACE+ '`' WORDS '`';
labelpart 				: LABEL WHITESPACE+ '`' WORDS '`';
titlepart 				: TITLE WHITESPACE+ '`' WORDS '`';
findpart 				: FIND WHITESPACE+ '`' CODE '`' (wherepart WHITESPACE+ | withinpart WHITESPACE+)* ifpart;
wherepart 				: WHERE WHITESPACE+ '`' WORDS '`';
withinpart 				: WITHIN WHITESPACE+ '`' WORD '`' WHITESPACE+ FIND WHITESPACE+ '`' CODE '`';
ifpart 					: IF (NEVER | NOT)? FOUND GENTLY? GIVE NO? FEEDBACK '(' feedbackpart ')' ;
feedbackpart 			: WORDS_NO_COMMA WHITESPACE* (COMMA WHITESPACE* WORDS_NO_COMMA)* ;

/*
 * Lexer rules
 */

fragment LOWERCASE 		: [a-z];
fragment UPPERCASE		: [A-Z];
fragment DIGIT 			: [0-9];
COMMA 					: ',';

WORDS 					: ~('`');
WORDS_NO_COMMA 			: ~(',' | ')');
WORDS_NO_HASH	 		: ~('#');
WORD 					: (LOWERCASE | UPPERCASE | DIGIT | '_' | '-')+ ;
CODE 					: ~('`');
WHITESPACE				: (' ' | '\t' | '\r'? '\n' | '\r'); 
BEGIN 					: 'BEGIN';
MESSAGE 				: 'MESSAGE';
LABEL 					: 'LABEL';
TITLE 					: 'TITLE';
FIND  					: 'FIND';
WHERE  					: 'WHERE';
WITHIN 					: 'WITHIN';
IF 						: 'IF';
NEVER 					: 'NEVER';
NOT 					: 'NOT';
FOUND  					: 'FOUND';
GENTLY 					: 'GENTLY' ;
GIVE 					: 'GIVE' ;
NO 						: 'NO' ;
FEEDBACK 				: 'FEEDBACK' ;
END 					: 'END';

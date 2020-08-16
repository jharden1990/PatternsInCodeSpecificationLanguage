lexer grammar specLang_draftP4Lexer;



//Default mode rules
OPEN_COMMENT			: '#'	-> mode(COMMENT);
OPEN_CODE				: '`'	-> pushMode(CODE);
OPEN_PARENS				: '('	-> mode(PARENS);
WHITESPACE				: [ \n\t\r]+ -> skip; 
BEGIN 					: 'BEGIN';
MESSAGE 				: 'MESSAGE';
LABEL 					: 'LABEL';
TITLE 					: 'TITLE';
FIND  					: 'FIND';
WHERE  					: 'WHERE';
WITHIN 					: 'WITHIN';
EXPRESSION				: ('__' (LOWERCASE | UPPERCASE | DIGIT)+ '__');
IF 						: 'IF';
//NEVER 					: 'NEVER';
NOT 					: 'NOT';
FOUND  					: 'FOUND';
GENTLE					: 'GENTLE' ;
GIVE 					: 'GIVE' ;
NO 						: 'NO' ;
FEEDBACK 				: 'FEEDBACK' ;
END 					: 'END';
ELSE					: 'ELSE';
WITHOUT					: 'WITHOUT';
WITH 					: 'WITH' ;
AS						: 'AS';
NAME					: (LOWERCASE | UPPERCASE | DIGIT | '_')+;


mode CODE;
CLOSE_CODE				: '`'	-> popMode;
CODE_TEXT				: ~('`')+;


mode COMMENT;
CLOSE_COMMENT			: '#'	-> mode(DEFAULT_MODE);
COMMENT_TEXT			: ~('#')+;

mode PARENS;
CLOSE_PARENS 			: ')'	-> mode(DEFAULT_MODE);
OPEN_CODE_IN_PARENS		: '`'	-> pushMode(CODE);
COMMA					: ',';
PARENS_TEXT				: ~(')' | '`' | ',' | ' ' | '\t' | '\n' | '\r')+;
WHITESPACE_PARENS		: [ \n\t\r]+ -> skip; 


fragment LOWERCASE 		: [a-z];
fragment UPPERCASE		: [A-Z];
fragment DIGIT 			: [0-9];



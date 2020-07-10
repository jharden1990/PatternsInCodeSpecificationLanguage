parser grammar specLang_draftP4Parser;
options {tokenVocab=specLang_draftP4Lexer;}

/*
 * Parser rules
 */

document				: statement+ EOF;
statement				: (beginpart messagespart findpart endpart | comment);
comment 				: OPEN_COMMENT COMMENT_TEXT CLOSE_COMMENT;
beginpart 				: BEGIN NAME OPEN_PARENS PARENS_TEXT? (COMMA PARENS_TEXT)* CLOSE_PARENS;
messagespart 			: messagepart labelpart titlepart;
messagepart 			: MESSAGE OPEN_CODE CODE_TEXT CLOSE_CODE;
labelpart 				: LABEL OPEN_CODE CODE_TEXT CLOSE_CODE;
titlepart 				: TITLE OPEN_CODE CODE_TEXT CLOSE_CODE;
findpart 				: findclause (whereclause | withinclause | ifclause | findclause)+ ;
findclause				: FIND OPEN_CODE CODE_TEXT CLOSE_CODE ;
whereclause 			: WHERE OPEN_CODE CODE_TEXT CLOSE_CODE ;
withinclause 			: WITHIN EXPRESSION FIND OPEN_CODE CODE_TEXT CLOSE_CODE ;
ifclause 				: IF NOT? FOUND feedbackpart elsepart? ;
elsepart 				: ELSE feedbackpart ; /* REMOVE THIS PART */
feedbackpart 			: (GIVE GENTLE? FEEDBACK (OPEN_PARENS feedbackparenspart? CLOSE_PARENS)? | GIVE NO FEEDBACK);
feedbackparenspart 		: (OPEN_CODE_IN_PARENS CODE_TEXT CLOSE_CODE | PARENS_TEXT) (COMMA (OPEN_CODE_IN_PARENS CODE_TEXT CLOSE_CODE | PARENS_TEXT))* ;
/* NOTE TO SELF: NEED TO FIX feedbackparenspart to not take in only 1 PARENS_TEXT OR ADD IN THE FORMAT PART(S)*/
endpart					: END (WITHOUT FEEDBACK | WITH GENTLE? FEEDBACK (OPEN_PARENS feedbackparenspart CLOSE_PARENS)?)? ;


/*
 * NOTES ON DIFFERENT CLAUSES
 * FIND (first find) finds matches of a pattern in the source code and returns a list of those matches.
 * WITHIN finds matches of a pattern within the expression given, which must have appeared in a prior find.
 * WHERE takes the set of matches produced by the most recent find and separates it into two categories, those which satisfy the pattern and those which do not.
 * Maybe need to have WHERE just return those which satisfy the pattern and expand the IF clause or add a WHEN clause for dealing with IF statements that want to run on first match.
 * Maybe make current IF clause the WHEN clause and have IF be a different clause for if statements that run on first match?
 * Maybe need to have WHERE return a list of objects which contain two parts: a boolean value representing whether the match fits the conditions, and the match pattern.
 */
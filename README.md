# Patterns in Code Specification Language (PiCSL)
Specification Language work for Pedal (PiCSL)

# How to Use
Make sure you have the ANTLR 4 runtime installed on your machine; the current version of this work is dependent on ANTLR 4.

To translate written PiCSL code into code usable by Pedal for Python, run the following command through the command line:
"> python PiCSLtoPedalCodeTranslator PiCSLcodeFile FeedbackWriteFile UnitTestWriteFile"
PiCSLtoPedalCodeTranslator = Translator file
PiCSLcodeFile = name of the file with the specification language code to be translated
FeedbackWriteFile = name of the file that you wish to write the translated feedback function code to
UnitTestWriteFile = name of the file that you wish to write the UnitTest environment code to; this argument is optional, and you probably don't need to use it unless you want a unit test version.

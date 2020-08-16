from pedal.environments.quick import *


def wrong_conversion_placement_1():
	MESSAGE = 'The input is always a string and must be converted to a number before being used in an arithmetic calculation.'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""
_var_ = input()
_var2_ = __expr__""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""_var_ * ___""", use_previous = match))
	prev_matchset = within0
	if not prev_matchset:
		return False
	where0 = []
	for match in prev_matchset:
		_var_ = match['_var_']
		if _var_.was_type('NumType'):
			where0.append(match)
	prev_matchset = where0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_conversion_placement_2():
	MESSAGE = 'The input is always a string and must be converted to a number before being used in an arithmetic calculation.'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""
_var_ = input()
_var2_ = __expr__""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""_var_ + ___""", use_previous = match))
	prev_matchset = within0
	if not prev_matchset:
		return False
	where0 = []
	for match in prev_matchset:
		_var_ = match['_var_']
		if _var_.was_type('NumType'):
			where0.append(match)
	prev_matchset = where0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_conversion_placement_3():
	MESSAGE = 'The conversion should be applied to result of the input operation.'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""input(float())""")
	prev_matchset = find0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_conversion_type():
	MESSAGE = 'The input is a number with a decimal point. The conversion should reflect this type of number.'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""int()""")
	prev_matchset = find0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def missing_float_conversion():
	MESSAGE = 'The input is always a string and must be converted to a number with decimals.'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""float()""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


from pedal.quick import *


def wrong_list_length_8_2():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""_list_ = __expr__""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		if __expr__.ast_name == "List" and len(__expr__.elts) < 3:
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def missing_list_initialization_8_2():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""shopping_cart = __expr__""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		if __expr__.ast_name == "List":
			where0.append(match)
	prev_matchset = where0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_list_is_constant_8_2():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""shopping_cart = __expr__""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		if __expr__.ast_name == "Num":
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_iteration_body_8_3():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item_ in _list_:\n    sum_length = ___ + ___\n""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_print_8_3():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item_ in _list_:\n    pass\nprint(_total_)""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def missing_target_slot_empty_8_4():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item_ in pages_count_list:\n    pass""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		_item_ = match['_item_']
		if _item_.id == "___":
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def missing_addition_slot_empty_8_4():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""sum_pages + _item_""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		_item_ = match['_item_']
		if _item_.id == "___":
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_names_not_agree_8_4():
	MESSAGE = 'Each value of <code>{0!s}</code> must be added to <code>{1!s}</code>.'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item1_ in pages_count_list:\n    sum_pages = sum_pages + _item2_""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		_item2_ = match['_item2_']
		_item1_ = match['_item1_']
		if _item1_.id != _item2_.id:
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(label=LABEL, title=TITLE, message=MESSAGE.format(_item1_.id, _item2_.id))
	return False


def wrong_modifying_list_8_5():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""[20473, 27630, 17849, 19032, 16378]""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_modifying_list_8_6():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""_list_ = [2.9, 1.5, 2.3, 6.1]""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_should_be_counting():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item_ in ___:\n    __expr__""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""___ = ___ + _item_""", use_previous = match))
	prev_matchset = within0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_should_be_summing():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item_ in ___:\n    __expr__""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""___ = 1 + ___""", use_previous = match))
	prev_matchset = within0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def missing_addition_slot_empty():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""___ + _item_""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		_item_ = match['_item_']
		if _item_.id == "___":
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_cannot_sum_list():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for ___ in _list_ :\n    __expr__""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""___ = ___ + _list_""", use_previous = match))
	prev_matchset = within0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def missing_no_print():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""print(___)""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def missing_counting_list():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item_ in ___:\n    __expr__""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""_sum_ = _sum_ + 1""", use_previous = match))
	prev_matchset = within0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def missing_summing_list():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item_ in ___:\n    __expr__""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""_sum_ = _sum_ + _item_""", use_previous = match))
	prev_matchset = within0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_printing_list():
	MESSAGE = 'You should be printing a single value.'
	LABEL = 'list_print'
	TITLE = 'Printing in Iteration'
	find0 = find_matches("""for ___ in ___:\n    __expr__""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""print(___)""", use_previous = match))
	prev_matchset = within0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def missing_average():
	MESSAGE = 'An average value is not computed.'
	LABEL = 'no_avg'
	TITLE = 'Missing Computation'
	find0 = find_matches("""for ___ in ___:\n    pass\n__expr__""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""_total_/_count_""", use_previous = match))
	prev_matchset = within0
	where0 = []
	for match in prev_matchset:
		_total_ = match['_total_']
		_count_ = match['_count_']
		if _total_.id != _count_.id:
			where0.append(match)
	prev_matchset = where0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def warning_average_in_iteration():
	MESSAGE = '("An average value is best computed after the properties name <code>{0!s}</code>(total) and <code>{1!s}</code> are completely known rather than recomputing the average on each iteration.")'
	LABEL = 'avg_in_iter'
	TITLE = 'Redundant Average Calculation'
	find0 = find_matches("""for ___ in ___:\n    __expr__\n""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""_average_ = _total_/_count_""", use_previous = match))
	prev_matchset = within0
	where0 = []
	for match in prev_matchset:
		_total_ = match['_total_']
		_average_ = match['_average_']
		_count_ = match['_count_']
		if _total_.id != _count_.id != _average_.id and _total_.id != _average_.id:
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(label=LABEL, title=TITLE, message=MESSAGE.format(_total_.id, _count_.id))
	return False


def wrong_average_denominator():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for ___ in ___:\n    __expr__\n__expr2__""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""_count_ = _count_ + 1""", use_previous = match))
	prev_matchset = within0
	within1 = []
	for match in prev_matchset:
		__expr2__ = match['__expr2__']
		within1.extend(__expr2__.find_matches("""___/_value_""", use_previous = match))
	prev_matchset = within1
	where0 = []
	for match in prev_matchset:
		_value_ = match['_value_']
		_count_ = match['_count_']
		if _count_.id != _value_.id:
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_average_numerator():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for ___ in ___:\n    __expr__\n__expr2__""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""_total_ = _total_ + _item_""", use_previous = match))
	prev_matchset = within0
	within1 = []
	for match in prev_matchset:
		__expr2__ = match['__expr2__']
		within1.extend(__expr2__.find_matches("""_value_/___""", use_previous = match))
	prev_matchset = within1
	where0 = []
	for match in prev_matchset:
		_total_ = match['_total_']
		_value_ = match['_value_']
		if _total_.id != _value_.id:
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_compare_list():
	MESSAGE = 'Each item in the list <code>{0!s}</code> must be compared one item at a time.'
	LABEL = 'comp_list'
	TITLE = 'Not Comparing Each Item'
	find0 = find_matches("""for ___ in _list_:\n    if __expr__:\n        pass""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		_list_ = match['_list_']
		__expr__ = match['__expr__']
		if __expr__.has(_list_.astNode):
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(label=LABEL, title=TITLE, message=MESSAGE.format(_list_.id))
	return False


def wrong_for_inside_if():
	MESSAGE = 'The iteration should not be inside the decision block.'
	LABEL = 'for_in_if'
	TITLE = 'For inside if'
	find0 = find_matches("""if ___:\n    for ___ in ___:\n        pass""")
	prev_matchset = find0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def iterator_is_function():
	MESSAGE = 'You should make a variable for the list instead of using a function call for the list.'
	LABEL = 'iter_is_func'
	TITLE = 'Using Function Call instead of List'
	find0 = find_matches("""for ___ in __funcCall__():\n    pass""")
	prev_matchset = find0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_list_initialization_9_1():
	MESSAGE = 'The list of rainfall amounts (<code>rainfall_list</code>) is not initialized properly.'
	LABEL = 'list_init_9.1'
	TITLE = 'Incorrect List Initialization'
	find0 = find_matches("""rainfall_list = weather.get("Data.Precipitation","Station.Location","Blacksburg, VA")""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_accumulator_initialization_9_1():
	MESSAGE = 'The variable to hold the total value of the rainfall amounts (<code>rainfall_sum</code>) is not initialized properly.'
	LABEL = 'accu_init_9.1'
	TITLE = 'Incorrect Accumulation Variable initialization'
	find0 = find_matches("""rainfall_sum = 0""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_accumulation_9_1():
	MESSAGE = 'The addition of each rainfall amount to <code>rainfall_sum</code> is not correct.'
	LABEL = 'accu_9.1'
	TITLE = 'Incorrect Accumulation Statement'
	find0 = find_matches("""rainfall_sum = _item_ + rainfall""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		_item_ = match['_item_']
		if _item_.id != "rainfall_sum":
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_list_initialization_placement_9_1():
	MESSAGE = 'The list of rainfall amount (<code>rainfall_list</code>) must be initialized before the iteration that uses this list.'
	LABEL = 'list_init_place_9.1'
	TITLE = 'List initialization Misplaced or Missing'
	find0 = find_matches("""rainfall_list = ___\nfor _item_ in _list_:\n    pass""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_accumulator_initialization_placement_9_1():
	MESSAGE = 'The variable for the sum of all the rainfall amounts (<code>rainfall_sum</code>) must be initialized before the iteration which uses this variable.'
	LABEL = 'accu_init_place_9.1'
	TITLE = 'Accumulator initialization Misplaced or missing'
	find0 = find_matches("""rainfall_sum = ___\nfor _item_ in _list_:\n    pass""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_iteration_body_9_1():
	MESSAGE = 'The addition of each rainfall amount to the total rainfall is not in the correct place.'
	LABEL = 'iter_body_9.1'
	TITLE = 'Accumulation Statement Misplaced or Missing'
	find0 = find_matches("""for _item_ in _list_:\n    rainfall_sum = ___""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_print_9_1():
	MESSAGE = 'The output of the total rainfall amount is not in the correct place. The total rainfall should be output only once after the total rainfall has been computed.'
	LABEL = 'print_9.1'
	TITLE = 'Print Statement Misplaced or Missing'
	find0 = find_matches("""for _item_ in _list_:\n    pass\nprint(_total_)""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_list_initialization_9_2():
	MESSAGE = 'The list of rainfall amounts (<code>rainfall_list</code>) is not initialized properly.'
	LABEL = 'list_init_9.2'
	TITLE = 'Incorrect List Initialization'
	find0 = find_matches("""rainfall_list = weather.get("Data.Precipitation","Station.Location","Blacksburg, VA")""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_accumulator_initialization_9_2():
	MESSAGE = 'The variable to hold the total value of the rainfall amounts (<code>rainfall_count</code>) is not initialized properly.'
	LABEL = 'accu_init_9.2'
	TITLE = 'Incorrect Initialization'
	find0 = find_matches("""rainfall_count = 0""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_accumulation_9_2():
	MESSAGE = 'The adding of another day with rainfall to the total count of days with rainfall (<code>rainfall_count</code>) is not correct.'
	LABEL = 'accu_9.2'
	TITLE = 'Accumulation Statement Incorrect'
	find0 = find_matches("""rainfall_count = _item_ + 1""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		_item_ = match['_item_']
		if _item_.id != "rainfall_count":
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_list_initialization_placement_9_2():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""rainfall_list = ___\nfor _item_ in _list_:\n    pass""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_accumulator_initialization_placement_9_2():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""rainfall_count = ___\nfor _item_ in _list_:\n    pass""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_iteration_body_9_2():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item_ in _list_:\n    if __expr__:\n        pass""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		if __expr__.numeric_logic_check(1, "var > 0"):
			where0.append(match)
	prev_matchset = where0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_decision_body_9_2():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""if __expr__:\n    rainfall_count = rainfall_count + 1""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		if __expr__.numeric_logic_check(1, "var > 0"):
			where0.append(match)
	prev_matchset = where0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_print_9_2():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item_ in _list_:\n    pass\nprint(_total_)""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_comparison_9_6():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""if __comp__:\n    pass""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		__comp__ = match['__comp__']
		if __comp__.numeric_logic_check(1, "var > 80") == False:
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_conversion_10_2():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _target_ in ___:\n    __expr__""")
	prev_matchset = find0
	if not prev_matchset:
		return False
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""_target_*0.04""", use_previous = match))
	prev_matchset = within0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_filter_condition_10_3():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""if __expr__:\n    pass""")
	prev_matchset = find0
	if not prev_matchset:
		return False
	where0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		if __expr__.numeric_logic_check(1, "var > 0") or __expr__.numeric_logic_check(1, "var != 0"):
			where0.append(match)
	prev_matchset = where0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_and_filter_condition_10_4():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _temp_ in _list_:\n    if __expr__:\n        pass""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		_temp_ = match['_temp_']
		__expr__ = match['__expr__']
		if (__expr__.has(_temp_.astNode) and not __expr__.numeric_logic_check(1, "32 <= temp <= 50")):
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_nested_filter_condition_10_4():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _temp_ in _list_:\n    if __cond1__:\n        if __cond2__:\n            pass""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		_temp_ = match['_temp_']
		__cond2__ = match['__cond2__']
		__cond1__ = match['__cond1__']
		if (__cond1__.has(_temp_.astNode) and __cond2__.has(_temp_.astNode) and (__cond1__.numeric_logic_check(1, "32 <= temp") and __cond2__.numeric_logic_check(1, "temp <= 50") or __cond2__.numeric_logic_check(1, "32 <= temp") and __cond1__.numeric_logic_check(1, "temp <= 50"))) == False:
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_conversion_problem_10_5():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item_ in ___:\n    __expr__""")
	prev_matchset = find0
	if not prev_matchset:
		return False
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""_item_*0.62""", use_previous = match))
	prev_matchset = within0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_filter_problem_atl1_10_5():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item_ in ___:\n    if __cond__:\n        _list_.append(__expr__)""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""_item_*0.62""", use_previous = match))
	prev_matchset = within0
	where0 = []
	for match in prev_matchset:
		_item_ = match['_item_']
		__cond__ = match['__cond__']
		if (__cond__.has(_item_.astNode) and not __cond__.numeric_logic_check(0.1, "item > 16.1290322580645")):
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_filter_problem_atl2_10_5():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item_ in ___:\n    _miles_ = __expr__\n    if __cond__:\n        _list_.append(_miles_)""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""_item_*0.62""", use_previous = match))
	prev_matchset = within0
	where0 = []
	for match in prev_matchset:
		_item_ = match['_item_']
		_miles_ = match['_miles_']
		__cond__ = match['__cond__']
		if not (__cond__.has(_miles_.astNode) and __cond__.numeric_logic_check(1, "_item_ > 10")):
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_append_problem_atl1_10_5():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item_ in ___:\n    if __cond__:\n        _list_.append(__expr__)""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		_item_ = match['_item_']
		__cond__ = match['__cond__']
		if (__cond__.numeric_logic_check(0.1, "item > 16.1290322580645") and __cond__.has(_item_.astNode)):
			where0.append(match)
	prev_matchset = where0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""_item_*0.62""", use_previous = match))
	prev_matchset = within0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_append_problem_atl2_10_5():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for _item_ in ___:\n    _miles_ = _item_ * 0.62\n    if __cond__:\n        _list_.append(_var_)""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		_miles_ = match['_miles_']
		_var_ = match['_var_']
		__cond__ = match['__cond__']
		if (__cond__.has(_miles_) and __cond__.numeric_logic_check(1, "_miles_ > 10")) and _var_.id != _miles_.id:
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_debug_10_7():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""filtered_sentence_counts = []\nbook_sentence_counts = classics.get("metrics.statistics.sentences","(None)","")\nfor book in book_sentence_counts:\n    if book >= 5000:\n        filtered_sentence_counts.append(book)\nplt.hist(filtered_sentence_counts)\nplt.title("Distribution of Number of Sentences in Long Books")\nplt.xlabel("Number of Sentences")\nplt.ylabel("Number of Long Books")\nplt.show()\n""")
	prev_matchset = find0
	if not prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_initialization_in_iteration():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""for ___ in ___:\n    __expr__""")
	prev_matchset = find0
	within0 = []
	for match in prev_matchset:
		__expr__ = match['__expr__']
		within0.extend(__expr__.find_matches("""_assign_ = __expr2__""", use_previous = match))
	prev_matchset = within0
	where0 = []
	for match in prev_matchset:
		__expr2__ = match['__expr2__']
		if len(__expr2__.find_all("Name")) == 0:
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_duplicate_var_in_add():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""_item_ + _item_""")
	prev_matchset = find0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def all_labels_present():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""plt.title(___)\nplt.show()""")
	prev_matchset = find0
	if not prev_matchset:
		return gently(message=MESSAGE, label=LABEL, title=TITLE)
	find1 = []
	for match in prev_matchset:
		find1.extend(find_matches("""plt.xlabel(___)\nplt.show()""", use_previous = match))
	prev_matchset = find1
	if not prev_matchset:
		return gently(message=MESSAGE, label=LABEL, title=TITLE)
	find2 = []
	for match in prev_matchset:
		find2.extend(find_matches("""plt.ylabel(___)\nplt.show()""", use_previous = match))
	prev_matchset = find2
	if not prev_matchset:
		return gently(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def show_parens():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""plt.show""")
	prev_matchset = find0
	if not prev_matchset:
		return False
	find1 = []
	for match in prev_matchset:
		find1.extend(find_matches("""plt.show()""", use_previous = match))
	prev_matchset = find1
	if not prev_matchset:
		return gently(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def hard_code_8_5():
	MESSAGE = 'message'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""print(__num__)""")
	prev_matchset = find0
	where0 = []
	for match in prev_matchset:
		__num__ = match['__num__']
		if len(__num__.find_all("Num")) > 0:
			where0.append(match)
	prev_matchset = where0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_conversion_placement_1():
	MESSAGE = 'The input is always a string and must be converted to a number before being used in an arithmetic calculation.'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""
_var_ = input()
= _var_ * ___""")
	prev_matchset = find0
	if prev_matchset:
		return explain(message=MESSAGE, label=LABEL, title=TITLE)
	return False


def wrong_conversion_placement_2():
	MESSAGE = 'The input is always a string and must be converted to a number before being used in an arithmetic calculation.'
	LABEL = 'label'
	TITLE = 'title'
	find0 = find_matches("""
_var_ = input()
= _var_ + ___""")
	prev_matchset = find0
	if prev_matchset:
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


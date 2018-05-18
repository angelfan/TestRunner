from module.Testcasegroup import Testcasegroup
from module.Testcase_testgroup import Testcase_testgroup
from module.Testcase import TestInterfacecase


def get_testcase_group(group_id):
    return Testcasegroup.query.get(group_id)


def get_testcase_by_group_id(group_id):

    test_group = get_testcase_group(group_id)
    testcase_testgroups = Testcase_testgroup.query.filter_by(testcase_group_id=group_id, is_active=True)

    testcases = []
    if test_group.testcase_type == 1:

        for testcase_testgroup in testcase_testgroups:
            testcase_id = testcase_testgroup.testcase_id
            testcase = TestInterfacecase.query.get(testcase_id)
            testcases.append(testcase)
    return testcases
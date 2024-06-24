#from test_suite import TestSuite
#import yaml
#from parse_submission import ParseSubmission
#import constants as c


#def validate_end_to_end_wflow():

  #  test_suite: TestSuite = TestSuite()

 #   data = yaml.safe_load(open('exampleWflowSubmissionFile.yml'))
 # all_parameters = ParseSubmission.get_parameters_from_submission(data)
  #  result: dict = test_suite.run_all(**all_parameters)

 #   assert result[c.SUITE_PASSED_ATTRIBUTE] is True


#def validate_end_to_end_leaky_bucket():

    #test_suite: TestSuite = TestSuite()

    #data = yaml.safe_load(open('exampleLeakyBucketSubmissionFile.yml'))
    #all_parameters = ParseSubmission.get_parameters_from_submission(data)
   # result: dict = test_suite.run_all(**all_parameters)

  #  assert result[c.SUITE_PASSED_ATTRIBUTE] is True

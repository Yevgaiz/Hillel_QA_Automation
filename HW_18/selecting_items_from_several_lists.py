test_design_writers = [1, 3, 5, 11, 12]
test_scripters = [1, 3, 4, 6, 7, 8, 12]
reviewers = [1, 2, 3, 9, 10, 12]
out_of_office_today = [2, 5]


all_testers = sorted(list(set(test_design_writers + test_scripters + reviewers)))

only_script_writers = sorted(list(set(test_scripters) - set(test_design_writers) - set(reviewers)))

at_work_today = sorted(list(set(all_testers) - set(out_of_office_today)))

write_and_review_at_work = sorted(list(set(test_scripters) & set(reviewers) & set(at_work_today)))

print(" All testers in the team\n", all_testers)
print("\n Testers who can only write scripts\n", only_script_writers)
print("\n Testers who are at work today\n", at_work_today)
print("\n Testers who could write and review scripts, and are at work today\n", write_and_review_at_work)

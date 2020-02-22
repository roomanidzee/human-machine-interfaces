
def test_files_retrieve(files_service):

    retrieve_result = files_service.retrieve_all_files()
    assert len(retrieve_result) != 0
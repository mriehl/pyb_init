def determine_project_name_from_git_url(git_url):
    start_index = git_url.rfind('/') + 1

    if git_url.endswith('.git'):
        end_index = len(git_url) - 4
    else:
        end_index = len(git_url)

    return git_url[start_index:end_index]

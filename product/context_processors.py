def add_variable_to_context(request):
    # uname = request.session['username']
    return {
        'cx_project': 'This is an ecommerce project',
        'cx_name': 'uname'
    }


# we can use {{cx_project}} or {{cx_name}} anywhere in the project like this wherever we want to print the values
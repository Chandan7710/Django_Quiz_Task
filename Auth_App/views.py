from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from Home_App.models import User
from Auth_App.models import QuesModel, QuesModelTwo, Leaderboard
from django.core.mail import send_mail
# Create your views here.

'''
Function For Profile Page
'''
def profile(request):
    return render(request, 'Auth_App/profile.html')


'''
Function For Registration Page
'''
def authregistration(request):
    
    '''Check if request.method is 'POST' from html'''
    if request.method == 'POST':
        
        '''Get the name, email, password, confirm_password from html page and get stored in
        the variables registration_username, registration_email,registration_password,
        registration_confirm_password respectively'''
        registration_username = request.POST['name']
        registration_email = request.POST['email']
        registration_password = request.POST['password']
        registration_confirm_password = request.POST['confirm_password']
        
        '''Check if password confirm_password are matches'''
        if registration_password == registration_confirm_password:
            
            '''Check user name already exists or not if exists display error message
            Username Already Exists'''
            if User.objects.filter(username=registration_username).exists():
                messages.error(request, 'Username Already Exists')
                
                '''Check user name already exists or not if exists display error message
                Username Already Exists'''
            elif User.objects.filter(email=registration_email).exists():
                messages.error(request, 'Email Already Exists')
                
            # Using User.objects.create_user user will be created is admin database
            else:
                registration_user = User.objects.create_user(username=registration_username, password=registration_password, email=registration_email)
                registration_user.save()
                messages.success(request, 'You have Successfully Registered')
                return redirect('login')
            
            '''If password confirm_password arent matches then errpr message
            Password and Conform Password Not Matched is displayed'''
        else:
            messages.error(request, 'Password and Conform Password Not Matched')
            
    '''registration.html page rendered to the user to get input from the user'''
    return render(request, 'Auth_App/registration.html')



'''
Function For Login
'''
def authlogin(request):
    
    '''Check if request.method is 'POST' from html'''
    if request.method == 'POST':
        
        '''Get the email, password from html page and get stored in variables
        login_email and login_password respectively'''
        login_email = request.POST['email']
        login_password = request.POST['password']
        
        '''authenticate will check for correct email and password'''
        auth_user = authenticate(request, email=login_email, password=login_password)

        '''If None is not stored in auth_user then user will successfully
        login and redirected to home page'''
        if auth_user is not None:
            login(request, auth_user)
            return redirect('profile')
        
        # To display error message for invalid Email or Password
        else:
            messages.error(request, 'Email or Password Invalid !')
        
    return render(request, 'Auth_App/login.html')


'''
Function For Logout
'''
def authlogout(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('login')


'''
Function For Quiz-1 Question and its Result
'''
def home(request):
    '''Check if request.method is 'POST' from html'''
    if request.method == 'POST':
        '''get all objects from QuesModel and stored in questions'''
        questions = QuesModel.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0 
        for q in questions:
            total += 1
            if q.ans == request.POST.get(q.question):
                # For correct marks 10 marks added
                score += 10
                correct += 1
            else:
                # For wrong answers 3 marks deducted
                wrong += 1
                score -= 3
        percent = score/(total*10) *100
        quiz_one_result = {
            'total': total,
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
        }
        
        '''Saving the Quiz result to database'''
        quiz_name =  "Quiz-1"
        user_name = request.user.username
        total_in_db = len(Leaderboard.objects.all())
        sl_no = str(total_in_db + 1)
        result = Leaderboard(sl_no = sl_no, name=user_name, quiz_name=quiz_name, 
                             total = total, correct=correct, 
                             incorrect=wrong, percentage=percent)
        result.save()
        
        # Email part
        send_mail("Your Quiz-1 Result", 
                  f"{quiz_one_result}",
                  "skill_test_quiz@result.com",
                  ["hachandan02@gmail.com", "byregowda@gmail.com", "hanumareddi02@gmail.com"])
        return render(request,'Auth_App/result.html', context = quiz_one_result)
    
    else:
        questions = QuesModel.objects.all()
        quiz_one_html_questions = {
            'questions': questions
        }
        return render(request,'Auth_App/quiz.html', context = quiz_one_html_questions)


'''
Function For Quiz-2 Question and its Result
'''
def quiz_two(request):
    '''Check if request.method is 'POST' from html'''
    if request.method == 'POST':
        quiz_two_questions = QuesModelTwo.objects.all()
        quiz_two_score = 0
        quiz_two_wrong = 0
        quiz_two_correct = 0
        quiz_two_total = 0
        for row in quiz_two_questions:
            quiz_two_total += 1
            if row.ans == request.POST.get(row.question):
                # For correct marks 10 marks added
                quiz_two_score += 10
                quiz_two_correct += 1
            else:
                # For wrong answers 3 marks deducted
                quiz_two_wrong += 1
                quiz_two_score -= 3
        quiz_two_percent = (quiz_two_score/(quiz_two_total*10)) * 100
        quiz_two_result = {
            'score': quiz_two_score,
            'correct': quiz_two_correct,
            'wrong': quiz_two_wrong,
            'percent': quiz_two_percent,
            'total': quiz_two_total,
            
        }
        
        '''Saving the Quiz result to database'''
        quiz_name =  "Quiz-2"
        user_name = request.user.username
        total_in_db = len(Leaderboard.objects.all())
        sl_no = str(total_in_db + 1)
        result = Leaderboard(sl_no = sl_no, name=user_name, quiz_name=quiz_name, 
                             total = quiz_two_total, correct=quiz_two_correct, 
                             incorrect=quiz_two_wrong, percentage=quiz_two_percent)
        result.save()
        
        # Email part
        send_mail("Your Quiz-2 Result", 
                  f"{quiz_two_result}",
                  "skill_test_quiz@result.com",
                  ["hachandan02@gmail.com", "byregowda@gmail.com", "hanumareddi02@gmail.com"])
        return render(request,'Auth_App/result_two.html', context = quiz_two_result)
    
    else:
        quiz_two_questions = QuesModelTwo.objects.all()
        quiz_two_html_questions = {
            'quiz_two_questions': quiz_two_questions
        }
        return render(request,'Auth_App/quiz_two.html', context = quiz_two_html_questions)
   
   
'''
To display the Leaderboard
''' 
def leader(request):
    result_list_board = Leaderboard.objects.order_by('sl_no')
    dict = {'heading': "The Last Quizz Results of People",
            'result_list': result_list_board}
    return render(request, 'Auth_App/leader.html', context = dict)
from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Choice, UserAnswer, UserProfile
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Choice, UserAnswer, UserProfile, Category

@login_required
def quiz_list(request):
    categories = Category.objects.all()
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes, 'categories': categories})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Choice, UserAnswer, UserProfile, Category

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()[:10]  # Show 10 questions per quiz

    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                choice = Choice.objects.get(id=selected_choice_id)
                UserAnswer.objects.create(user=request.user, question=question, choice=choice)
                if choice.is_correct:
                    score += 1

        total_marks = len(questions)  # Total possible marks
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_profile.score += score
        user_profile.save()

        if score == total_marks:  # Check if the user scored 100%
            return redirect('certificate')  # Redirect to the certificate page

        return render(request, 'quiz_result.html', {
            'score': score,
            'total': total_marks,
            'percentage': (score / total_marks) * 100
        })

    return render(request, 'quiz_detail.html', {'quiz': quiz, 'questions': questions})
@login_required
def certificate(request):
    return render(request, 'certificate.html', {'user': request.user})


from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import os
import pandas as pd
import numpy as np
import json
import joblib

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from fitness_app.models import WorkoutList

# Create views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'mtarget.pkl')
regressor = os.path.join(BASE_DIR, 'modelrg.pkl')

# Unpickle Model
model = joblib.load(model_path)
modelrg = joblib.load(regressor)


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if form.save():
                messages.success(request, 'Account was created')
                return redirect('Login')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

    context = {'form': form}
    return render(request, 'register.html', context)


# Create views here.
def index(request):
    if request.method == "POST":
        bodyPart_ARMS = 0
        bodyPart_LEGS = 0
        bodyPart_TRUNK = 0

        weight = request.POST["inputWeights"]
        reps = request.POST["inputReps"]

        if request.POST["inputBodyPart"] == 'ARMS':
            bodyPart_ARMS = 1
        elif request.POST["inputBodyPart"] == 'LEGS':
            bodyPart_LEGS = 1
        elif request.POST["inputBodyPart"] == 'TRUNK':
            bodyPart_TRUNK = 1

        df = np.asarray([weight, reps, bodyPart_ARMS, bodyPart_LEGS, bodyPart_TRUNK]).reshape(1, -1)
        df = pd.DataFrame(df, columns=['Weight', 'Reps', 'BodyPart_ARMS', 'BodyPart_LEGS', 'BodyPart_TRUNK'])

        prediction = model.predict(df)
        result = prediction[0]
        context = {'result': result}
        return render(request, "home.html", context)
    else:
        context = {}
        return render(request, "home.html", context)


def predict(request):
    if request.method == "POST":
        bpbarbell = 0
        bordbell = 0
        bcbarbell = 0
        bcdumbell = 0
        cu = 0
        curldumbell = 0
        cyc = 0
        dl = 0
        dbarbell = 0
        dtbar = 0
        fpull = 0
        fsbbell = 0
        ge = 0
        gm = 0
        gmbb = 0
        hs = 0
        hcurl = 0
        hcdbell = 0
        hhra = 0
        hrwg = 0
        hbrwa = 0
        hlpd = 0
        hsr = 0
        srcg = 0
        hspress = 0
        inclinebp = 0
        inbpbarbell = 0
        inpdumb = 0
        lpulldown = 0
        lraise = 0
        lrdumb = 0
        lcurl = 0
        lofly = 0
        lpress = 0
        lphinge = 0
        liddbell = 0
        mpstand = 0
        nu = 0
        opbbell = 0
        opdbell = 0
        pull = 0
        rp2 = 0
        dfly = 0
        rdbarbell = 0
        scrow = 0
        smpress = 0
        smpdbell = 0
        sr = 0
        sspbbell = 0
        sspdbell = 0
        spstand = 0
        ssbench = 0
        squat = 0
        barbell = 0
        tbar = 0
        triex = 0
        tripush = 0
        wdips = 0
        cgbench = 0
        hbsquat = 0
        kswings = 0

        exercise = request.POST["predict"]

        if exercise == 'Bench Press (Barbell)':
            bpbarbell = 1
        elif exercise == 'Bent Over Row (Dumbbell)':
            bordbell = 1
        elif exercise == 'Bicep Curl (Barbell)':
            bcbarbell = 1
        elif exercise == 'Bicep Curl (Dumbbell)':
            bcdumbell = 1
        elif exercise == 'Chin Up':
            cu = 1
        elif exercise == 'Curl Dumbbell':
            curldumbell = 1
        elif exercise == 'Cycling':
            cyc = 1
        elif exercise == 'Deadlift':
            dl = 1
        elif exercise == 'Deadlift (Barbell)':
            dbarbell = 1
        elif exercise == 'Deadlift - Trap Bar':
            dtbar = 1
        elif exercise == 'Face pull':
            fpull = 1
        elif exercise == 'Front Squat (Barbell)':
            fsbbell = 1
        elif exercise == 'Glute extension. ':
            ge = 1
        elif exercise == 'Good Morning':
            gm = 1
        elif exercise == 'Good Morning (Barbell)':
            gmbb = 1
        elif exercise == 'Hack Squat':
            hs = 1
        elif exercise == 'Hammer Curl':
            hcurl = 1
        elif exercise == 'Hammer Curl (Dumbbell )':
            hcdbell = 1
        elif exercise == 'Hammer High Row - 1 Arm':
            hhra = 1
        elif exercise == 'Hammer Row - Wide Grip':
            hrwg = 1
        elif exercise == 'Hammer back row wide 45 angle':
            hbrwa = 1
        elif exercise == 'Hammer lat pulldown':
            hlpd = 1
        elif exercise == 'Hammer seated row':
            hsr = 1
        elif exercise == 'Hammer seated row (CLOSE GRIP)':
            srcg = 1
        elif exercise == 'Hammer shoulder press':
            hspress = 1
        elif exercise == 'Incline Bench Press':
            inclinebp = 1
        elif exercise == 'Incline Bench Press (Barbell)':
            inbpbarbell = 1
        elif exercise == 'Incline Press (Dumbbell)':
            inpdumb = 1
        elif exercise == 'Lat Pulldown':
            lpulldown = 1
        elif exercise == 'Lateral Raise':
            lraise = 1
        elif exercise == 'Lateral Raise (Dumbbells)':
            lrdumb = 1
        elif exercise == 'Leg curl':
            lcurl = 1
        elif exercise == 'Leg outward fly':
            lofly = 1
        elif exercise == 'Leg press':
            lpress = 1
        elif exercise == 'Leg press (hinge )':
            lphinge = 1
        elif exercise == 'Low Incline Dumbbell Bench':
            liddbell = 1
        elif exercise == 'Military Press (Standing)':
            mpstand = 1
        elif exercise == 'Neutral Chin':
            nu = 1
        elif exercise == 'Overhead Press (Barbell)':
            opbbell = 1
        elif exercise == 'Overhead Press (Dumbbell)':
            opdbell = 1
        elif exercise == 'Pull Up':
            pull = 1
        elif exercise == 'Rack Pull 2 Pin':
            rp2 = 1
        elif exercise == 'Rear delt fly':
            dfly = 1
        elif exercise == 'Romanian Deadlift (Barbell)':
            rdbarbell = 1
        elif exercise == 'Seated Cable Row (close Grip)':
            scrow = 1
        elif exercise == 'Seated Military Press':
            smpress = 1
        elif exercise == 'Seated Military Press (Dumbbell)':
            smpdbell = 1
        elif exercise == 'Seated Row':
            sr = 1
        elif exercise == 'Seated Shoulder Press (Barbell)':
            sspbbell = 1
        elif exercise == 'Seated Shoulder Press (Dumbbell)':
            sspdbell = 1
        elif exercise == 'Shoulder Press (Standing)':
            spstand = 1
        elif exercise == 'Sling Shot Bench':
            ssbench = 1
        elif exercise == 'Squat':
            squat = 1
        elif exercise == 'Squat (Barbell)':
            barbell = 1
        elif exercise == 'T-bar Row':
            tbar = 1
        elif exercise == 'Tricep Extension':
            triex = 1
        elif exercise == 'Tricep pushdown':
            tripush = 1
        elif exercise == 'Weighted dips':
            wdips = 1
        elif exercise == 'close grip Bench':
            cgbench = 1
        elif exercise == 'high bar squat':
            hbsquat = 1
        elif exercise == 'kettlebell Swings':
            kswings = 1

        print(exercise)

        df2 = np.asarray(
            [bpbarbell, bordbell, bcbarbell, bcdumbell, cu, curldumbell, cyc, dl, dbarbell, dtbar, fpull, fsbbell, ge, gm, gmbb, hs, hcurl, hcdbell, hhra, hrwg, hbrwa,
            hlpd, hsr, srcg, hspress, inclinebp, inbpbarbell, inpdumb, lpulldown, lraise, lrdumb, lcurl, lofly, lpress, lphinge, liddbell, mpstand, nu, opbbell, opdbell,
            pull, rp2, dfly, rdbarbell, scrow, smpress, smpdbell, sr, sspbbell, sspdbell, spstand, ssbench, squat, barbell, tbar, triex, tripush , wdips, cgbench, hbsquat, kswings

        ]).reshape(1, -1)
        df2 = pd.DataFrame(df2, columns=['ExerciseName_Bench Press (Barbell)', 'ExerciseName_Bent Over Row (Dumbbell)',
                                          'ExerciseName_Bicep Curl (Barbell)', 'ExerciseName_Bicep Curl (Dumbbell)', 'ExerciseName_Chin Up',
                                          'ExerciseName_Curl Dumbbell', 'ExerciseName_Cycling', 'ExerciseName_Deadlift',
                                          'ExerciseName_Deadlift (Barbell)', 'ExerciseName_Deadlift - Trap Bar', 'ExerciseName_Face pull',
                                          'ExerciseName_Front Squat (Barbell)', 'ExerciseName_Glute extension. ', 'ExerciseName_Good Morning',
                                          'ExerciseName_Good Morning (Barbell)', 'ExerciseName_Hack Squat', 'ExerciseName_Hammer Curl',
                                          'ExerciseName_Hammer Curl (Dumbbell )', 'ExerciseName_Hammer High Row - 1 Arm', 'ExerciseName_Hammer Row - Wide Grip',
                                          'ExerciseName_Hammer back row wide 45 angle', 'ExerciseName_Hammer lat pulldown', 'ExerciseName_Hammer seated row',
                                          'ExerciseName_Hammer seated row (CLOSE GRIP)', 'ExerciseName_Hammer shoulder press', 'ExerciseName_Incline Bench Press',
                                          'ExerciseName_Incline Bench Press (Barbell)', 'ExerciseName_Incline Press (Dumbbell)', 'ExerciseName_Lat Pulldown',
                                          'ExerciseName_Lateral Raise', 'ExerciseName_Lateral Raise (Dumbbells)', 'ExerciseName_Leg curl', 'ExerciseName_Leg outward fly',
                                          'ExerciseName_Leg press', 'ExerciseName_Leg press (hinge )', 'ExerciseName_Low Incline Dumbbell Bench',
                                          'ExerciseName_Military Press (Standing)', 'ExerciseName_Neutral Chin', 'ExerciseName_Overhead Press (Barbell)',
                                          'ExerciseName_Overhead Press (Dumbbell)', 'ExerciseName_Pull Up', 'ExerciseName_Rack Pull 2 Pin', 'ExerciseName_Rear delt fly',
                                          'ExerciseName_Romanian Deadlift (Barbell)', 'ExerciseName_Seated Cable Row (close Grip)', 'ExerciseName_Seated Military Press',
                                          'ExerciseName_Seated Military Press (Dumbbell)', 'ExerciseName_Seated Row', 'ExerciseName_Seated Shoulder  Press (Barbell)',
                                          'ExerciseName_Seated Shoulder Press (Dumbbell)', 'ExerciseName_Shoulder Press (Standing)', 'ExerciseName_Sling Shot Bench',
                                          'ExerciseName_Squat', 'ExerciseName_Squat (Barbell)', 'ExerciseName_T-bar Row', 'ExerciseName_Tricep Extension',
                                          'ExerciseName_Tricep pushdown', 'ExerciseName_Weighted dips', 'ExerciseName_close grip Bench', 'ExerciseName_high bar squat',
                                          'ExerciseName_kettlebell Swings'])
        prediction2 = modelrg.predict(df2)
        result2 = prediction2[0]
        # print(result2)
        context2 = {'result2': result2}
        return render(request, "home.html", context2)
    else:
        context2 = {}
        return render(request, "home.html", context2)


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Username or password is incorrect")

    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('/')


def workout_list(request):
    user = request.user
    print('list')

    if request.user.is_authenticated:
        my_list = WorkoutList.objects.filter(user=user)
        print(my_list)
        context = {'my_list': my_list}
        return render(request, "workouts.html", context)
    else:
        messages.error(request, 'You need to be logged in')

    return redirect('/')


def add_workout(request):
    user = request.user
    print(user)
    print('add')

    if request.user.is_authenticated:

        if request.method == 'POST':
            print(request.POST)
            workouts = request.POST.getlist('workout')

            for wk in workouts:
                workout = WorkoutList()
                workout.workout = wk
                workout.user = user
                workout.save()

            messages.success(request, 'Workout added to list')
    else:
        messages.error(request, 'You need to be logged in')

    return redirect('/')


def delete_workout(request):
    user = request.user
    print(user)
    print('del')

    if request.user.is_authenticated:
        workout_id = request.GET['id']
        workout = WorkoutList.objects.get(id=workout_id)
        print(workout)
        workout.delete()
        messages.success(request, 'Workout deleted')
    else:
        messages.error(request, 'You need to be logged in')

    return redirect('/workout')



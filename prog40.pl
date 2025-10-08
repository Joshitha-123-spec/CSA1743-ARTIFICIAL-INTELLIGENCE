% Facts: diseases and their symptoms
disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(headache),
    symptom(sore_throat).

disease(cold) :-
    symptom(runny_nose),
    symptom(sneezing),
    symptom(sore_throat).

disease(typhoid) :-
    symptom(fever),
    symptom(abdominal_pain),
    symptom(headache).

disease(malaria) :-
    symptom(fever),
    symptom(chills),
    symptom(sweating).

% Ask user for symptoms and diagnose
diagnose :-
    write('Enter patient symptoms followed by a period.'), nl,
    read_symptoms,
    ( disease(D) ->
        write('The patient may have: '), write(D), nl
    ; write('No matching disease found.'), nl ).

% Read symptoms until 'stop.' entered
read_symptoms :-
    repeat,
    write('Symptom (or type stop.): '),
    read(X),
    ( X == stop -> ! ;
      assert(symptom(X)), fail ).

UPDATE ---> Today updated some test cases for more accurate tests.

Build a RESTful API for a simple note-taking application using Django Framework
Ae per above Assessment question i completed the given task I’ve thoroughly reviewed the requirements 
and ensured that all components are addressed to the best of my ability.

Assessment Details
NoteTaking_api -- Project Name
Note_app -- Aplication Name
Api -- (i) Serializers
      (ii) Urls.py
     (iii) Views.py

As per Assesment question for better Api expericnce there is swagger to test all api's
 http://127.0.0.1:8000/note/swagger/  ---> uisng this swagger Url user can use all api functionality


Links for DjangoRestFramework UI    
Api EndPoints and there localhost address
(i) CreateNoteView  --->  http://127.0.0.1:8000/note/Api/  
    user can create there new own notes uing this Url

(ii) FetchNotesbyIDView ---> http://127.0.0.1:8000/note/Api/1/
    User can fetch there notes by there userID or use any id in this Url
    
(iii) SearchQueryNotesView --->  http://127.0.0.1:8000/note/Api/?search=LordKrishna/
    User can search any notes related there 'title' using this Url
    
(iv) UpdateNoteView  ---> http://127.0.0.1:8000/note/Api/update/1/
    User can Update there notes using perticular ID using thus Url

For Test cases for every endpoints please refer Note_app test.py file.
Case(i) --> test_createnote, 
Case(ii) --> test_NoteById, 
Case(iii) --> test_NoteByTitle, 
Case(iv) --> test_UpdateNote, 




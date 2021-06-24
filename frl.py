def c():
    #potrzebne moduły(instaluj przez 'pip install nazwa'):

    #face_recognition
    import face_recognition
    #opencv-python
    import cv2
    #numpy (instaluje się automatycznie z opencv)
    import numpy as np

    #ustawienie kamery na pierwszą możliwą
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Załaduj obraz i naucz się rozpowzawać obrazy
    #można zmieniać i dodawać kolejne (zmieniając 'grabowski' lub kopiująć dwie kolejne linie)
    grabowski_image = face_recognition.load_image_file("grabowski.jpg") #podaj nazwę zdjęcia (z pełną sćieżką jeśli tak jest łatwiej) 
    grabowski_face_encoding = face_recognition.face_encodings(grabowski_image)[0] 


    # Tworzy 2 jsony:
    # kody z rozpozanwania twarzy
    known_face_encodings = [
        grabowski_face_encoding

   
    ]
    # i ich nazwy
    known_face_names = [
        "Krzysiu"
        
    ]
    #muszą być w kolejnośći (np. [a_face, b_face] i [a_name, b_name]
    #dodawaj po przecinku, najlepiej z enterem np:
    #known_face_names = [
    #    "Krzysiu",
    #    "Zbysiu"
    #]
    
    
    
    
    # Zmienne
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    
    while True:
        # Bierze klatkę z kamery
        ret, frame = video_capture.read()
    
        # Zmniejsza klatke do 1/4 wielkości dla prędkości
        small_frame = cv2.resize(frame, (0, 0), fx=0.2, fy=0.2)
    
        # Konweruje z BRG (używane przez OpenCV) na RGB (używane przec face-recognition)
        rgb_small_frame = small_frame[:, :, ::-1]
    
        # Sprawdza co drugą klatkę
        if process_this_frame:
            # Znajduje wszystkie twarze i je rozpoznaje
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # Sprawdza czy zna jakieś twarze
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                #Jeśli nie zna:
                name = "Unknown"
    
                #wsm nie wiem co to robi
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
    
                face_names.append(name)
                if (name == 'Krzysiu'):
                    video_capture.release()
                    cv2.destroyAllWindows()
                    return 'True'
                    break
        process_this_frame = not process_this_frame
    
    
        # Wyświetla wyniki
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Zwraca normalny rozmiar, wcześniej zmniejszyło do 0.25
            top *= 5
            right *= 5
            bottom *= 5
            left *= 5
    
            # Rysuje kwadrat wokól twarzy
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
            # Podpisuje twarz
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    
        # wyświetla w oknie wynik
        
    
        # kliknij q żeby wyjść
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Po wyjściu deaktywuje kamerę i niszczy okno opencv
    video_capture.release()
    cv2.destroyAllWindows()
        

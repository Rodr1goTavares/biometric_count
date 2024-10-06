import cv2
import mediapipe as mp

class HandCapture:
    def __init__(self, connection_obj):
        self._connection = connection_obj
        self._cv2_video = self._connection.open_and_get_cv2()
        self._mp_hands = mp.solutions.hands
        self._hands = self._mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self._mp_drawing = mp.solutions.drawing_utils
        
    def start_capture(self):
        while self._cv2_video.isOpened():
            ret, frame = self._cv2_video.read()
            if not ret:
                break
            # Convert to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            processedFrame = self._hands.process(image)
            
            # Return to BGR
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Se mãos forem detectadas
            if processedFrame.multi_hand_landmarks:
                for hand_landmarks in processedFrame.multi_hand_landmarks:
                    # Desenhar os landmarks
                    self._mp_drawing.draw_landmarks(image, hand_landmarks, self._mp_hands.HAND_CONNECTIONS)

                    # Contar os dedos levantados
                    fingers = self._calcFingersPosition(hand_landmarks)
                    cv2.putText(image, f'Dedos levantados: {fingers}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    print("Dedos levantados: " + str(fingers))

            # Exibir o frame com a detecção
            cv2.imshow('Hand Tracking', image)

            # Sair do loop se a tecla 'q' for pressionada
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Liberar recursos
        self._connection.close_cv2()
        pass

    def _calcFingersPosition(self, hand_landmarks):
        # Índices dos dedos
        thumb_tip = hand_landmarks.landmark[self._mp_hands.HandLandmark.THUMB_TIP]
        thumb_ip = hand_landmarks.landmark[self._mp_hands.HandLandmark.THUMB_IP]

        index_tip = hand_landmarks.landmark[self._mp_hands.HandLandmark.INDEX_FINGER_TIP]
        index_dip = hand_landmarks.landmark[self._mp_hands.HandLandmark.INDEX_FINGER_DIP]

        middle_tip = hand_landmarks.landmark[self._mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        middle_dip = hand_landmarks.landmark[self._mp_hands.HandLandmark.MIDDLE_FINGER_DIP]

        ring_tip = hand_landmarks.landmark[self._mp_hands.HandLandmark.RING_FINGER_TIP]
        ring_dip = hand_landmarks.landmark[self._mp_hands.HandLandmark.RING_FINGER_DIP]

        pinky_tip = hand_landmarks.landmark[self._mp_hands.HandLandmark.PINKY_TIP]
        pinky_dip = hand_landmarks.landmark[self._mp_hands.HandLandmark.PINKY_DIP]

        wrist = hand_landmarks.landmark[self._mp_hands.HandLandmark.WRIST]
    
        fingers_up = 0
        if thumb_tip.x > thumb_ip.x:
            fingers_up += 1

        if index_tip.y < index_dip.y:
            fingers_up += 1
        if middle_tip.y < middle_dip.y:
            fingers_up += 1
        if ring_tip.y < ring_dip.y:
            fingers_up += 1
        if pinky_tip.y < pinky_dip.y:
            fingers_up += 1

        return fingers_up

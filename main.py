import frl
running = True
while running:
    test = frl.c()
    if test:
        print('Idzie')
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

input()





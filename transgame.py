import pygame

Ancho=840
Alto=680
VERDE=[0,255,0]
BLANCO=[255,255,255]
NEGRO=[0,0,0]

def traslacion(t, p):
	x = t[0]+p[0]
	y = t[1]+p[1]
	return [x, y]


if __name__=='__main__':
    pygame.init()
    var=0
    flag=0
    p1=[50,50]
    p2=[100,50]
    p3=[50,100]
    reloj=pygame.time.Clock()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    pygame.draw.polygon(pantalla,VERDE,[p1,p2,p3])
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    var=-2
                    flag=1
                elif event.key==pygame.K_RIGHT:
                    var=2
                    flag=1
                elif event.key==pygame.K_UP:
                    var=-2
                    flag=2
                elif event.key==pygame.K_DOWN:
                    var=2
                    flag=2
                elif event.key==pygame.K_SPACE:
                    var=0
                    flag=0

        if(flag==0):
            pantalla.fill(NEGRO)
            pygame.draw.polygon(pantalla,VERDE,[p1,p2,p3])
            pygame.display.flip()
        elif(flag==1):
            pantalla.fill(NEGRO)
            p1=traslacion(p1,[var,0])
            p2=traslacion(p2,[var,0])
            p3=traslacion(p3,[var,0])
            pygame.draw.polygon(pantalla,VERDE,[p1,p2,p3])
            pygame.display.flip()
        elif(flag==2):
            pantalla.fill(NEGRO)
            p1=traslacion(p1,[0,var])
            p2=traslacion(p2,[0,var])
            p3=traslacion(p3,[0,var])
            pygame.draw.polygon(pantalla,VERDE,[p1,p2,p3])
            pygame.display.flip()
        reloj.tick(200)

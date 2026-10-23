import glfw
from OpenGL.GL import *
import math


def desenhar_ceu():
    glColor3f(0.5, 0.75, 0.95)
    glBegin(GL_QUADS)
    glVertex2f(-10, 0.0)
    glVertex2f(10, 0.0)
    glVertex2f(10, 7.5)
    glVertex2f(-10, 7.5)
    glEnd()


def desenhar_circulo(cx, cy, raio):
    glBegin(GL_POLYGON)
    segmentos = 40
    for i in range(segmentos):
        ang = 2.0 * math.pi * i / segmentos
        glVertex2f(cx + math.cos(ang) * raio, cy + math.sin(ang) * raio)
    glEnd()


def desenhar_sol():
    glColor3f(1.0, 0.95, 0.55)
    desenhar_circulo(0.5, 0.8, 1.5)


def desenhar_floresta_ao_fundo():
    glColor3f(0.35, 0.45, 0.35)
    
    glBegin(GL_QUADS)
    glVertex2f(-10, -0.2)
    glVertex2f(10, -0.2)
    glVertex2f(10, 0.5)
    glVertex2f(-10, 0.5)
    glEnd()

    glBegin(GL_TRIANGLES)
    for i in range(-10, 10):
        glVertex2f(i, 0.5)
        glVertex2f(i + 1, 0.5)
        glVertex2f(i + 0.5, 1.1 + 0.3 * math.sin(i * 1.7))
    glEnd()


def desenhar_grama():
    glColor3f(0.65, 0.7, 0.1)
    
    glBegin(GL_QUADS)
    glVertex2f(-10, 0.0)
    glVertex2f(10, 0.0)
    glVertex2f(10, -7.5)
    glVertex2f(-10, -7.5)
    glEnd()


def desenhar_arvore():
    
    glColor3f(0.2, 0.12, 0.08)

    # tronco (GL_QUADS)
    glBegin(GL_QUADS)
    glVertex2f(-0.25, 0.0)
    glVertex2f(0.25, 0.0)
    glVertex2f(0.12, 3.0)
    glVertex2f(-0.12, 3.0)
    glEnd()

    # galhos (GL_LINES)
    glLineWidth(3.0)
    glBegin(GL_LINES)
    # galhos grossos
    glVertex2f(0, 1.8);  glVertex2f(-1.2, 3.4)
    glVertex2f(0, 2.3);  glVertex2f(1.3, 3.8)
    glVertex2f(0, 3.0);  glVertex2f(-0.7, 4.6)
    glVertex2f(0, 3.0);  glVertex2f(0.9, 4.7)
    glEnd()

    glLineWidth(1.5)
    glBegin(GL_LINES)
    # galhos finos
    glVertex2f(-1.2, 3.4); glVertex2f(-2.0, 3.9)
    glVertex2f(-1.2, 3.4); glVertex2f(-1.5, 4.4)
    glVertex2f(1.3, 3.8);  glVertex2f(2.1, 4.2)
    glVertex2f(1.3, 3.8);  glVertex2f(1.2, 4.9)
    glVertex2f(-0.7, 4.6); glVertex2f(-1.2, 5.3)
    glVertex2f(0.9, 4.7);  glVertex2f(1.4, 5.4)
    glVertex2f(0.0, 5.0);  glVertex2f(-0.2, 5.5)
    glEnd()


def desenhar_sombra_arvore():
    """Sombra comprida em direção a nós (o sol está atrás)"""
    glColor3f(0.25, 0.35, 0.03)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.25, 0.0)
    glVertex2f(0.25, 0.0)
    glVertex2f(-1.2, -4.5)
    glEnd()


def desenhar_arvore_completa(x, y, escala, inclinacao=0.0, espelhar=False):
    """Usa Translate + Rotate + Scale (+ espelhamento) para reaproveitar a árvore"""
    # sombra
    glPushMatrix()
    glTranslatef(x, y, 0.0)
    glScalef(escala, escala, 1.0)
    desenhar_sombra_arvore()
    glPopMatrix()

    # árvore
    glPushMatrix()
    glTranslatef(x, y, 0.0)
    glRotatef(inclinacao, 0.0, 0.0, 1.0)
    glScalef(-escala if espelhar else escala, escala, 1.0)
    desenhar_arvore()
    glPopMatrix()


def desenhar_casa():
    """Casa/celeiro desenhada na origem (canto inferior esquerdo)"""
    # sombra da casa
    glColor3f(0.25, 0.35, 0.03)
    glBegin(GL_QUADS)
    glVertex2f(0.0, 0.0)
    glVertex2f(4.0, 0.0)
    glVertex2f(2.5, -3.5)
    glVertex2f(-1.5, -3.5)
    glEnd()

    # parede (GL_QUADS)
    glColor3f(0.55, 0.48, 0.40)
    glBegin(GL_QUADS)
    glVertex2f(0.0, 0.0)
    glVertex2f(4.0, 0.0)
    glVertex2f(4.0, 2.5)
    glVertex2f(0.0, 2.5)
    glEnd()

    # telhado (GL_TRIANGLES)
    glColor3f(0.45, 0.2, 0.18)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.4, 2.5)
    glVertex2f(4.4, 2.5)
    glVertex2f(2.0, 4.2)
    glEnd()

    # porta
    glColor3f(0.25, 0.17, 0.12)
    glBegin(GL_QUADS)
    glVertex2f(0.4, 0.0)
    glVertex2f(1.4, 0.0)
    glVertex2f(1.4, 1.7)
    glVertex2f(0.4, 1.7)
    glEnd()

    # janela
    glColor3f(0.3, 0.4, 0.5)
    glBegin(GL_QUADS)
    glVertex2f(2.5, 1.0)
    glVertex2f(3.5, 1.0)
    glVertex2f(3.5, 1.9)
    glVertex2f(2.5, 1.9)
    glEnd()


def main():
    if not glfw.init():
        return

    janela = glfw.create_window(800, 600, "Paisagem com OpenGL", None, None)
    if not janela:
        return glfw.terminate()

    glfw.make_context_current(janela)
    glfw.swap_interval(1)

    print("Paisagem com OpenGL...")

    while not glfw.window_should_close(janela):
        glfw.poll_events()

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-10, 10, -7.5, 7.5, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # ORDEM DE DESENHO: do fundo para a frente
        desenhar_ceu()
        desenhar_sol()
        desenhar_floresta_ao_fundo()
        desenhar_grama()

        # Árvores (mais longe = menor e mais alta na tela)
        desenhar_arvore_completa(-2.0, -1.2, 0.6, inclinacao=3)
        desenhar_arvore_completa(2.5, -1.4, 0.7, inclinacao=-4, espelhar=True)
        desenhar_arvore_completa(-5.0, -2.0, 0.9, inclinacao=-3)

        # Casa à direita (Translate + Scale)
        glPushMatrix()
        glTranslatef(5.3, -1.6, 0.0)
        glScalef(0.95, 0.95, 1.0)
        desenhar_casa()
        glPopMatrix()

        # Árvores da frente (maiores)
        desenhar_arvore_completa(-8.0, -3.5, 1.5, inclinacao=-4)
        desenhar_arvore_completa(4.5, -3.0, 1.0, inclinacao=5, espelhar=True)

        glfw.swap_buffers(janela)

    glfw.terminate()


if __name__ == "__main__":
    main()
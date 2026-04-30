# 🚀 Space Invaders Hybridge - Guía del Proyecto

¡Bienvenido al proyecto de **Space Invaders**! Este juego ha sido desarrollado utilizando **Python** y la librería **Pygame**. Esta guía está diseñada para que tú, como alumno, comprendas no solo cómo jugar, sino cómo está construido el código detrás de la pantalla.

---

## 🛠️ Requisitos e Instalación

Para ejecutar este proyecto, necesitas tener instalado Python en tu computadora.

1. **Instalar Pygame**: Abre tu terminal o consola y ejecuta el siguiente comando:
   ```bash
   pip install pygame
   ```

2. **Ejecutar el Juego**: Navega hasta la carpeta del proyecto y ejecuta el archivo principal:
   ```bash
   python main.py
   ```

---

## 🎮 Cómo Jugar (Controles)

El objetivo es simple: destruye a los enemigos antes de que lleguen a la parte inferior de la pantalla.

*   **Movimiento**: Usa las **Flechas del teclado** o las teclas **W, A, S, D**.
*   **Disparar**: Presiona la tecla **Espacio**.
*   **Menú**: Navega por los menús usando el mouse para seleccionar opciones como "Jugar", "Puntajes" o "Acerca de".

---

## 🧠 Lógica del Proyecto (Arquitectura)

Este proyecto utiliza el paradigma de **Programación Orientada a Objetos (POO)**. Aquí te explicamos las piezas clave:

### 1. Clases Principales
*   **`Game` (GameClass.py)**: Es el "cerebro" del juego. Controla las vidas, el nivel actual, la carga de puntajes máximos y el HUD (la interfaz que ves arriba con las vidas y nivel).
*   **`Player` (PlayerClass.py)**: Hereda de una clase base `Ship`. Controla el movimiento del jugador, la creación de balas y el sistema de "cooldown" (tiempo de espera entre disparos).
*   **`Enemy` (EnemyClass.py)**: Gestiona el comportamiento de los enemigos, su velocidad y cómo aparecen en oleadas.
*   **`Bullet` (BulletClass.py)**: Define las propiedades de los proyectiles y detecta colisiones con los enemigos.

### 2. El Ciclo de Juego (Main Loop)
En `main.py` encontrarás el corazón del programa. Funciona en tres pasos constantes:
1.  **Entrada (Events)**: Detecta si presionaste una tecla o cerraste la ventana.
2.  **Actualización (Update)**: Mueve al jugador, mueve a los enemigos, detecta si una bala golpeó a un enemigo y revisa si pasaste de nivel.
3.  **Dibujo (Draw)**: Limpia la pantalla y vuelve a dibujar todo en su nueva posición. ¡Esto sucede 60 veces por segundo (60 FPS)!

### 3. Sistema de Niveles y Dificultad
A medida que eliminas a todos los enemigos:
*   El nivel aumenta.
*   Los enemigos se vuelven más rápidos.
*   Cada 3 niveles, tu nave recibe mejoras como mayor capacidad de balas o una vida extra.

### 4. Persistencia de Datos
El juego lee y escribe en el archivo `puntajes.txt`. Esto permite que tu récord se guarde incluso después de cerrar el juego.

---

## 🌟 Retos para Alumnos (Mejoras Sugeridas)

Si quieres practicar y mejorar este proyecto, intenta lo siguiente:
1.  **Nuevos Enemigos**: Crea un tipo de enemigo que dispare de vuelta.
2.  **Power-ups**: Haz que aparezcan objetos que te den triple disparo o escudo temporal.
3.  **Sonidos**: Cambia los efectos de sonido en la carpeta `/sounds`.
4.  **Fondos Dinámicos**: Haz que el fondo se mueva para dar una sensación de velocidad.

---

**¡Diviértete programando y explorando el espacio!** 🛸✨

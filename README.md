<h1 align="center">LANDING PAGE</h1>

<p align="center">Landing page desarrollada en html y css con estilos modernos, un ejemplo clásico para que aprendaás a crear una landing para tu emprendimiento.</p>

<p align="center">
  <img src="https://img.shields.io/badge/licencia-MAC-green" alt="Licencia MIT">
  <img src="https://img.shields.io/badge/versi%C3%B3n-1.0.0-blue" alt="Versión">
  <img src="https://img.shields.io/badge/contribuidores-2-brightgreen" alt="Contribuidores">
</p>

## Índice de Contenido
1. [Introducción](#introducción)
2. [Estructura de la Landing Page](#estructura-de-la-landing-page)
3. [Visualización](#visualización)
4. [Tecnologías Empleadas](#tecnologías-empleadas)
5. [Codificación](#codificación)

---

## Introducción
Este proyecto web tiene como objetivo desarrollar una landing page optimizada y visualmente atractiva que sirva como primera impresión para visitantes y potenciales clientes. La página combinará diseño moderno, contenido relevante y una experiencia de usuario fluida para captar la atención desde el primer momento y guiar al usuario hacia la acción deseada, ya sea suscribirse, descargar un recurso o contactar al equipo. Además, se implementarán técnicas de SEO y un diseño responsive para asegurar que la página sea fácilmente accesible desde cualquier dispositivo, maximizando su alcance y efectividad.

En este proyecto, cada sección de la página está pensada para transmitir el mensaje principal de la marca y sus beneficios, utilizando una estructura clara y un diseño que fomente la navegación intuitiva. El resultado será una landing page funcional y persuasiva, lista para impulsar los objetivos de marketing y atraer a la audiencia correcta.

## Estructura de la Landing Page
En esta sección se describe la estructura general de la Landing Page, incluyendo las diferentes secciones y su propósito. Por ejemplo:

- **Header**: Contiene el menú horizontal y un botón de inicio de sesión.
- **Sección info**: Una zona de ofertas, formulario de contacto para envío de artículos exclusivos e imagen alusiva a la tienda.
- **Sección productos**: Visualización tipo tarjetas de los últimos productos en la tienda.
- **Sección noticias y contacto**: Invitación a los clientes para continuar en contacto en caso de algún requerimiento.
- **Footer**: Las redes sociales, mapa del sitio  y Copyright


## Visualización
Se detallan las consideraciones de diseño y usabilidad de la Landing Page, incluyendo aspectos como:

- **Diseño Responsivo**: La Landing Page se adaptada a diferentes dispositivos móviles facilitando su visualización.
- **Paleta de Colores**: Se utilizaron conceptos de psicología del color y diseño gráfico para internet a fin de generar una experiencia de usuario inigualable.
- **Tipografía**: Se incorporaron estilos vanguardista a través de tailwingcss para generar una mejor experiencia del lectura a los visitantes.
- **Imágenes y Multimedia**: Las imágenes han sido incorporados a través del serevicio de Freepik.

A continuación se presenta en imágen la representación de la Langing Page:

![](https://github.com/monicarias/Landing-page/blob/main/Prototipo.jpg?raw=true)

## Tecnologías Empleadas
La principal tecnología empleada es tailwingcss, este framework permite construir interfaces de usuario de manera rápida y eficiente utilizando una metodología de "utility-first". En lugar de escribir código CSS personalizado para cada componente, Tailwind ofrece una amplia gama de clases predefinidas que se pueden aplicar directamente en el HTML para estilizar elementos. Estas clases están diseñadas para controlar aspectos como el espaciado, el tamaño, los colores, la tipografía y otros estilos visuales, lo que facilita la creación de diseños consistentes y totalmente personalizables sin necesidad de escribir CSS desde cero. Además, Tailwind permite una fácil personalización y escalabilidad, ya que las clases son modulares y pueden adaptarse a proyectos de cualquier tamaño.

## Codificación
Aquí se proporcionarán algunos aldetalles sobre el proceso de desarrollo del código, incluyendo estructuras básicas, componentes y funcionalidades clave implementadas en la landing page, como ejemplo nos centraremos en la primera sección que es el header:

```
<!DOCTYPE html>
<!-- Documento HTML principal que define la estructura de la página web -->

<!-- Este archivo se guardó desde la URL especificada -->
<!-- saved from url=(0045)https://landingpagemarcablanca.netlify.app/?# -->

<html lang="en">
<head>
    <!-- Metadatos de la página -->
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <!-- Configuración de compatibilidad para navegadores antiguos -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!-- Vista adaptable a dispositivos móviles -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Enlace al archivo CSS de Tailwind para estilos predefinidos -->
    <link href="./U Guitars_files/tailwind.min.css" rel="stylesheet">
    <title>U Guitars</title> <!-- Título de la página que aparece en la pestaña del navegador -->
</head>
<body>
<div class="bg-white"> <!-- Contenedor principal con fondo blanco -->
    <div class="relative overflow-hidden"> <!-- Contenedor que permite contenido desbordado -->
      
      <!-- Inicio de la sección del encabezado -->
      <header class="relative">
        <div class="bg-gray-900 pt-6"> <!-- Fondo del encabezado en gris oscuro -->
          
          <!-- Barra de navegación principal -->
          <nav class="relative max-w-7xl mx-auto flex items-center justify-between px-4 sm:px-6" aria-label="Global">
            <div class="flex items-center flex-1"> <!-- Contenedor de los elementos de navegación -->
              
              <!-- Logo y menú de navegación para dispositivos pequeños -->
              <div class="flex items-center justify-between w-full md:w-auto">
                
                <!-- Botón de menú para dispositivos móviles -->
                <div class="-mr-2 flex items-center md:hidden">
                  <button type="button" class="bg-gray-900 rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:bg-gray-800 focus:outline-none focus:ring-2 focus-ring-inset focus:ring- white" aria-expanded="false">
                    <span class="sr-only">Open main menu</span> <!-- Texto accesible para lectores de pantalla -->
                    
                    <!-- Ícono de menú de hamburguesa para dispositivos móviles -->
                    <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                  </button>
                </div>
              </div>
              
              <!-- Enlaces de navegación visibles en dispositivos grandes -->
              <div class="hidden space-x-8 md:flex md:ml-10">
                <a href="https://landingpagemarcablanca.netlify.app/?#" class="text-base font-medium text-white hover:text-gray-300">Catálogo</a>
                <a href="https://landingpagemarcablanca.netlify.app/?#" class="text-base font-medium text-white hover:text-gray-300">¿Quiénes somos?</a>
                <a href="https://landingpagemarcablanca.netlify.app/?#" class="text-base font-medium text-white hover:text-gray-300">Contacto</a>
              </div>
            </div>
            
            <!-- Enlace de Iniciar Sesión para dispositivos grandes -->
            <div class="hidden md:flex md:items-center md:space-x-6">
              <a href="https://landingpagemarcablanca.netlify.app/?#" class="text-base font-medium text-white hover:text-gray-300">
                Iniciar sesión
              </a>
            </div>
          </nav>
        </div>
      </header> <!-- Fin de la sección del encabezado -->

```

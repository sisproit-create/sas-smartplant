export default function SASSmartPlantLandingPage() {
  const features = [
    {
      title: "Control de Diésel",
      text: "Conciliación del flujo P2 → Hyundai → equipos, validación automática y detección de diferencias operativas.",
    },
    {
      title: "Control AC30",
      text: "Inventario, recepciones, consumo por producción y alertas de desbalance en tiempo real.",
    },
    {
      title: "Producción y Eficiencia",
      text: "Toneladas producidas, consumo por tonelada, tendencias operativas y visibilidad diaria para gerencia.",
    },
    {
      title: "Alertas Inteligentes",
      text: "Desviaciones detectadas automáticamente con recomendaciones accionables para reducir pérdidas y mejorar decisiones.",
    },
  ];

  const metrics = [
    { label: "Producción analizada", value: "1,734 ton" },
    { label: "Combustible Diésel usado", value: "4,700 gal" },
    { label: "Asfalto (AC30) usado", value: "52,000 kg" },
    { label: "Alertas activas", value: "3" },
  ];

  const steps = [
    "Captura datos operativos diarios",
    "Valida inventarios, consumos y flujos",
    "Detecta desviaciones automáticamente",
    "Genera alertas y reportes claros",
  ];

  const problemPoints = [
    "Falta de control en diésel",
    "Desbalance en AC30",
    "Errores manuales en producción",
    "Falta de trazabilidad en calidad",
    "Reportes tardíos o inexactos",
  ];

  const solutionPoints = [
    "Captura datos en tiempo real",
    "Valida automáticamente la información",
    "Detecta desviaciones y pérdidas",
    "Genera alertas inteligentes",
    "Automatiza reportes",
    "Optimiza la toma de decisiones",
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      {/* HERO */}
      <section className="relative overflow-hidden border-b border-white/10">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(59,130,246,0.18),transparent_30%),radial-gradient(circle_at_left,rgba(16,185,129,0.12),transparent_25%)]" />
        <div className="relative mx-auto flex min-h-screen max-w-7xl items-center px-6 py-16 lg:px-8">
          <div className="grid w-full items-center gap-16 lg:grid-cols-2">
            {/* COLUMNA IZQUIERDA */}
            <div>
              <div className="mb-4 inline-flex items-center rounded-full border border-sky-400/30 bg-sky-400/10 px-3 py-1 text-sm text-sky-300">
                Inteligencia operativa para plantas de asfalto
              </div>

              <h1 className="max-w-4xl -mt-2 text-5xl font-bold tracking-tight text-white sm:text-6xl lg:text-7xl">
                SAS SmartPlant
              </h1>

              <p className="mt-6 max-w-2xl text-lg leading-9 text-slate-300">
                Control total de diésel, AC30, producción y calidad en tiempo real para reducir pérdidas,
                mejorar la visibilidad operativa y acelerar decisiones en planta.
              </p>

              <div className="mt-8 flex flex-wrap gap-4">
                <a
                  href="https://sas-smartplant-nfhbmqb39yeacmngdyan4i.streamlit.app/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="rounded-2xl bg-sky-500 px-5 py-3 text-sm font-semibold text-white shadow-lg shadow-sky-500/20 transition hover:bg-sky-400"
                >
                  Ver demo
                </a>

                <a
                  href="#contacto"
                  className="rounded-2xl border border-white/15 px-5 py-3 text-sm font-semibold text-slate-200 transition hover:bg-white/5"
                >
                  Solicitar presentación
                </a>
              </div>

              <div className="mt-10 grid max-w-2xl grid-cols-2 gap-4 sm:grid-cols-4">
                {metrics.map((item) => (
                  <div
                    key={item.label}
                    className="rounded-2xl border border-white/10 bg-white/5 p-4 backdrop-blur-sm"
                  >
                    <div className="text-2xl font-bold text-white">{item.value}</div>
                    <div className="mt-1 text-sm text-slate-400">{item.label}</div>
                  </div>
                ))}
              </div>
            </div>

            {/* COLUMNA DERECHA */}
            <div
              id="demo"
              className="rounded-[28px] border border-white/10 bg-slate-900/80 p-5 shadow-2xl shadow-sky-900/20 backdrop-blur lg:scale-105"
            >
              <div className="rounded-[24px] border border-white/10 bg-slate-950 p-5">
                <div className="mb-5 flex items-center justify-between">
                  <div>
                    <div className="text-sm text-slate-400">Dashboard operativo</div>
                    <div className="text-xl font-semibold">Resumen operativo</div>
                  </div>
                  <div className="rounded-full bg-emerald-500/15 px-3 py-1 text-sm text-emerald-300">
                    Activo
                  </div>
                </div>

                <div className="grid grid-cols-2 gap-3">
                  <div className="rounded-2xl bg-slate-900 p-4">
                    <div className="text-sm text-slate-400">Producción analizada</div>
                    <div className="mt-1 text-2xl font-bold">1,734 ton</div>
                    <div className="mt-2 text-sm text-emerald-300">Período analizado</div>
                  </div>

                  <div className="rounded-2xl bg-slate-900 p-4">
                    <div className="text-sm text-slate-400">Combustible Diésel usado</div>
                    <div className="mt-1 text-2xl font-bold">4,700 gal</div>
                    <div className="mt-2 text-sm text-rose-300">Consumo registrado</div>
                  </div>

                  <div className="rounded-2xl bg-slate-900 p-4">
                    <div className="text-sm text-slate-400">Asfalto (AC30) usado</div>
                    <div className="mt-1 text-2xl font-bold">52,000 kg</div>
                    <div className="mt-2 text-sm text-amber-300">Desviación vs diseño</div>
                  </div>

                  <div className="rounded-2xl bg-slate-900 p-4">
                    <div className="text-sm text-slate-400">Alertas activas</div>
                    <div className="mt-1 text-2xl font-bold">3</div>
                    <div className="mt-2 text-sm text-rose-300">Alta prioridad</div>
                  </div>
                </div>

                <div className="mt-4 rounded-2xl border border-rose-400/20 bg-rose-500/10 p-4">
                  <div className="text-sm font-semibold text-rose-300">Alerta crítica</div>
                  <div className="mt-1 text-sm text-slate-200">
                    La diferencia entre despacho Hyundai y distribución a equipos es de 300 gal.
                  </div>
                </div>

                <div className="mt-4 grid gap-3 lg:grid-cols-2">
                  <div className="rounded-2xl bg-slate-900 p-4">
                    <div className="text-sm text-slate-400">Flujo de Combustible Diésel</div>
                    <div className="mt-3 space-y-3">
                      {[
                        ["Recepción P2", "10,000 gal", "100%"],
                        ["Despacho Hyundai", "8,500 gal", "85%"],
                        ["Distribución Equipos", "8,200 gal", "82%"],
                      ].map(([label, value, width]) => (
                        <div key={label}>
                          <div className="mb-1 flex items-center justify-between text-sm">
                            <span className="text-slate-300">{label}</span>
                            <span className="text-white">{value}</span>
                          </div>
                          <div className="h-2 rounded-full bg-slate-800">
                            <div
                              className="h-2 rounded-full bg-sky-400"
                              style={{ width }}
                            />
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>

                  <div className="rounded-2xl bg-slate-900 p-4">
                    <div className="text-sm text-slate-400">Recomendación del sistema</div>
                    <p className="mt-3 text-sm leading-7 text-slate-200">
                      Revisar humedad de agregados, tiempos muertos, temperatura de operación y conciliación del flujo P2 → Hyundai → Equipos antes del cierre diario.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* VIDEOS */}
      <section className="mx-auto max-w-7xl px-6 py-20 lg:px-8">
        <div className="mx-auto max-w-3xl text-center">
          <div className="inline-flex rounded-full border border-sky-400/20 bg-sky-500/10 px-3 py-1 text-sm text-sky-300">
            Videos
          </div>

          <h2 className="mt-5 text-3xl font-bold tracking-tight text-white sm:text-4xl">
            SAS SmartPlant en acción
          </h2>

          <p className="mt-4 text-lg text-slate-400">
            Entiende el problema, la solución y el sistema en minutos.
          </p>
        </div>

        <div className="mt-12 grid gap-8 md:grid-cols-2 xl:grid-cols-3">
          {/* VIDEO 1 */}
          <div className="group overflow-hidden rounded-[28px] border border-white/10 bg-black/60 shadow-[0_20px_80px_rgba(0,0,0,0.35)]">
            <div className="relative aspect-video overflow-hidden bg-black">
              <video
                autoPlay
                muted
                loop
                playsInline
                controls
                preload="metadata"
                poster="https://res.cloudinary.com/dzkcqhndy/video/upload/so_0/pitch_pvthvb.jpg"
                className="h-full w-full object-cover object-[center_10%] transition duration-700 ease-out group-hover:scale-[1.05]"
              >
                <source
                  src="https://res.cloudinary.com/dzkcqhndy/video/upload/q_auto,f_auto/pitch_pvthvb.mp4"
                  type="video/mp4"
                />
              </video>

              <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent" />
            </div>

            <div className="border-t border-white/10 bg-black/70 px-5 py-4">
              <div className="text-sm font-medium text-slate-200">
                Pitch general del sistema
              </div>
            </div>
          </div>

          {/* VIDEO 2 */}
          <div className="group overflow-hidden rounded-[28px] border border-white/10 bg-black/60 shadow-[0_20px_80px_rgba(0,0,0,0.35)]">
            <div className="relative aspect-video overflow-hidden bg-black">
              <video
                autoPlay
                muted
                loop
                playsInline
                controls
                preload="metadata"
                poster="https://res.cloudinary.com/dzkcqhndy/video/upload/so_0/problema_icynkd.jpg"
                className="h-full w-full object-cover object-[center_10%] transition duration-700 ease-out group-hover:scale-[1.05]"
              >
                <source
                  src="https://res.cloudinary.com/dzkcqhndy/video/upload/q_auto,f_auto/problema_icynkd.mp4"
                  type="video/mp4"
                />
              </video>

              <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent" />
            </div>

            <div className="border-t border-white/10 bg-black/70 px-5 py-4">
              <div className="text-sm font-medium text-slate-200">
                Problema: pérdidas ocultas
              </div>
            </div>
          </div>

          {/* VIDEO 3 */}
          <div className="group overflow-hidden rounded-[28px] border border-white/10 bg-black/60 shadow-[0_20px_80px_rgba(0,0,0,0.35)]">
            <div className="relative aspect-video overflow-hidden bg-black">
              <video
                autoPlay
                muted
                loop
                playsInline
                controls
                preload="metadata"
                poster="https://res.cloudinary.com/dzkcqhndy/video/upload/so_0/solucion_lnyfh8.jpg"
                className="h-full w-full object-cover object-[center_10%] transition duration-700 ease-out group-hover:scale-[1.05]"
              >
                <source
                  src="https://res.cloudinary.com/dzkcqhndy/video/upload/q_auto,f_auto/solucion_lnyfh8.mp4"
                  type="video/mp4"
                />
              </video>

              <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent" />
            </div>

            <div className="border-t border-white/10 bg-black/70 px-5 py-4">
              <div className="text-sm font-medium text-slate-200">
                Solución: inteligencia operativa
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* PROBLEMA */}
      <section className="border-b border-white/10 bg-slate-900/60">
        <div className="mx-auto max-w-6xl px-6 py-20 lg:px-8">
          <div className="mx-auto max-w-3xl text-center">
            <div className="inline-flex rounded-full border border-rose-400/20 bg-rose-500/10 px-3 py-1 text-sm text-rose-300">
              Problema
            </div>
            <h2 className="mt-5 text-3xl font-bold tracking-tight text-white sm:text-4xl">
              Las plantas pierden dinero todos los días sin verlo a tiempo
            </h2>
            <p className="mt-4 text-lg text-slate-400">
              Especialmente en asfalto y construcción, una parte importante de las pérdidas proviene de
              controles dispersos, conciliaciones tardías y decisiones tomadas con información incompleta.
            </p>
          </div>

          <div className="mt-12 grid gap-5 md:grid-cols-2 xl:grid-cols-3">
            {problemPoints.map((item) => (
              <div
                key={item}
                className="rounded-3xl border border-white/10 bg-white/[0.03] p-6 text-slate-200 shadow-lg shadow-black/20"
              >
                {item}
              </div>
            ))}
          </div>

          <div className="mt-12 grid gap-6 lg:grid-cols-3">
            <div className="rounded-3xl border border-rose-400/20 bg-rose-500/10 p-6">
              <div className="text-sm text-rose-300">Impacto real</div>
              <div className="mt-2 text-3xl font-bold text-white">$5,000 – $50,000</div>
              <div className="mt-2 text-slate-300">en pérdidas ocultas mensuales</div>
            </div>

            <div className="rounded-3xl border border-white/10 bg-white/[0.03] p-6">
              <div className="text-sm text-slate-400">Consecuencia</div>
              <div className="mt-2 text-xl font-semibold text-white">Decisiones sin datos confiables</div>
              <div className="mt-2 text-slate-400">La operación depende de revisiones tardías y conciliaciones manuales.</div>
            </div>

            <div className="rounded-3xl border border-white/10 bg-white/[0.03] p-6">
              <div className="text-sm text-slate-400">Resultado</div>
              <div className="mt-2 text-xl font-semibold text-white">Baja eficiencia operativa</div>
              <div className="mt-2 text-slate-400">Se pierde tiempo, visibilidad y capacidad de reacción.</div>
            </div>
          </div>
        </div>
      </section>

      {/* VISIÓN */}
      <section className="mx-auto max-w-7xl px-6 py-20 lg:px-8">
        <div className="mx-auto max-w-3xl text-center">
          <div className="inline-flex rounded-full border border-sky-400/20 bg-sky-500/10 px-3 py-1 text-sm text-sky-300">
            Visión del sistema
          </div>
          <h2 className="mt-5 text-3xl font-bold tracking-tight text-white sm:text-4xl">
            No solo guarda datos, piensa sobre la operación
          </h2>
          <p className="mt-4 text-lg text-slate-400">
            SAS SmartPlant está diseñado para convertir datos operativos dispersos en control, alertas y decisiones accionables.
          </p>
        </div>

        <div className="mt-12 grid gap-6 md:grid-cols-2 xl:grid-cols-4">
          {[
            ["1", "Capturar datos"],
            ["2", "Validar y cruzar información"],
            ["3", "Detectar problemas"],
            ["4", "Generar acciones y reportes"],
          ].map(([num, text]) => (
            <div
              key={num}
              className="rounded-3xl border border-white/10 bg-white/[0.03] p-6 shadow-lg shadow-black/20"
            >
              <div className="flex h-12 w-12 items-center justify-center rounded-full bg-sky-500/15 text-lg font-bold text-sky-300">
                {num}
              </div>
              <div className="mt-4 text-lg font-semibold text-white">{text}</div>
            </div>
          ))}
        </div>
      </section>

      {/* SOLUCIÓN */}
      <section className="border-y border-white/10 bg-white/[0.02]">
        <div className="mx-auto max-w-6xl px-6 py-20 lg:px-8">
          <div className="mx-auto max-w-3xl text-center">
            <div className="inline-flex rounded-full border border-emerald-400/20 bg-emerald-500/10 px-3 py-1 text-sm text-emerald-300">
              Solución
            </div>
            <h2 className="mt-5 text-3xl font-bold tracking-tight text-white sm:text-4xl">
              Una sola plataforma para controlar toda la operación
            </h2>
            <p className="mt-4 text-lg text-slate-400">
              Desde combustible y AC30 hasta producción, calidad y alertas inteligentes.
            </p>
          </div>

          <div className="mt-12 grid gap-5 md:grid-cols-2 xl:grid-cols-3">
            {solutionPoints.map((item) => (
              <div
                key={item}
                className="rounded-3xl border border-white/10 bg-slate-900/60 p-6 text-slate-200"
              >
                {item}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CASO REAL */}
      <section className="w-full border-t border-white/10 bg-slate-950 px-6 py-20 md:px-12">
        <div className="mx-auto max-w-7xl">
          <div className="mb-14 max-w-3xl">
            <div className="mb-5 inline-flex items-center rounded-full border border-cyan-400/30 bg-cyan-400/10 px-4 py-1 text-sm text-cyan-300">
              Caso real en operación
            </div>

            <h2 className="text-3xl font-bold leading-tight tracking-tight text-white md:text-5xl">
              Validado en operación real,
              <span className="text-cyan-400"> no en teoría</span>
            </h2>

            <p className="mt-5 text-lg leading-8 text-slate-300">
              Implementado en una planta de asfalto en Panamá, SAS SmartPlant permitió
              detectar diferencias operativas, mejorar el control del flujo de diésel y
              aumentar la visibilidad de la operación en tiempo real.
            </p>
          </div>

          <div className="mb-10 grid grid-cols-1 gap-8 lg:grid-cols-2">
            <div className="rounded-2xl border border-red-500/20 bg-white/5 p-8 backdrop-blur-sm">
              <div className="mb-4 flex items-center gap-3">
                <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-red-500/15 text-xl text-red-400">
                  ⚠️
                </div>
                <h3 className="text-2xl font-semibold text-white">Problema real</h3>
              </div>

              <p className="mb-5 leading-7 text-slate-300">
                Antes de SAS SmartPlant, la planta operaba con controles manuales y
                reportes tardíos, lo que dificultaba la toma de decisiones en tiempo real.
              </p>

              <ul className="space-y-3 text-slate-300">
                <li className="flex gap-3">
                  <span className="text-red-400">•</span>
                  <span>Diferencias de diésel no detectadas a tiempo</span>
                </li>
                <li className="flex gap-3">
                  <span className="text-red-400">•</span>
                  <span>Desbalance en consumo de asfalto (AC30)</span>
                </li>
                <li className="flex gap-3">
                  <span className="text-red-400">•</span>
                  <span>Falta de trazabilidad operativa inmediata</span>
                </li>
                <li className="flex gap-3">
                  <span className="text-red-400">•</span>
                  <span>Dependencia de análisis manual</span>
                </li>
              </ul>
            </div>

            <div className="rounded-2xl border border-cyan-500/20 bg-white/5 p-8 backdrop-blur-sm">
              <div className="mb-4 flex items-center gap-3">
                <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-cyan-500/15 text-xl text-cyan-400">
                  ⚙️
                </div>
                <h3 className="text-2xl font-semibold text-white">Solución aplicada</h3>
              </div>

              <p className="mb-5 leading-7 text-slate-300">
                Implementamos SAS SmartPlant como sistema de control inteligente para
                capturar, validar y analizar la operación en tiempo real.
              </p>

              <ul className="space-y-3 text-slate-300">
                <li className="flex gap-3">
                  <span className="text-cyan-400">•</span>
                  <span>Captura de datos en tiempo real</span>
                </li>
                <li className="flex gap-3">
                  <span className="text-cyan-400">•</span>
                  <span>Validación automática de flujos</span>
                </li>
                <li className="flex gap-3">
                  <span className="text-cyan-400">•</span>
                  <span>Detección automática de desviaciones</span>
                </li>
                <li className="flex gap-3">
                  <span className="text-cyan-400">•</span>
                  <span>Dashboard operativo para toma de decisiones</span>
                </li>
              </ul>
            </div>
          </div>

          <div className="mb-10 rounded-2xl border border-emerald-500/20 bg-emerald-500/5 p-8">
            <div className="mb-4 flex items-center gap-3">
              <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-emerald-500/15 text-xl text-emerald-400">
                📊
              </div>
              <h3 className="text-2xl font-semibold text-white">Resultados observados</h3>
            </div>

            <div className="grid grid-cols-1 gap-4 text-slate-200 md:grid-cols-2">
              <div className="rounded-xl border border-white/10 bg-white/5 p-5">
                Identificación de diferencias operativas previamente invisibles
              </div>
              <div className="rounded-xl border border-white/10 bg-white/5 p-5">
                Mejora en el control del flujo de diésel
              </div>
              <div className="rounded-xl border border-white/10 bg-white/5 p-5">
                Validación de consistencia operativa
              </div>
              <div className="rounded-xl border border-white/10 bg-white/5 p-5">
                Reducción del tiempo de análisis
              </div>
            </div>
          </div>

          <div className="mb-12 grid grid-cols-1 gap-8 lg:grid-cols-2">
            <div className="rounded-2xl border border-amber-400/20 bg-amber-400/5 p-8">
              <h3 className="mb-5 text-2xl font-semibold text-white">
                Ejemplo real detectado por el sistema
              </h3>

              <div className="space-y-4 leading-7 text-slate-300">
                <div className="rounded-xl border border-white/10 bg-white/5 p-4">
                  <span className="font-medium text-amber-300">Producción baja</span>
                  <p className="mt-2">
                    El sistema puede identificar días con producción atípica que distorsionan
                    los indicadores por tonelada y requieren revisión operativa.
                  </p>
                </div>

                <div className="rounded-xl border border-white/10 bg-white/5 p-4">
                  <span className="font-medium text-amber-300">Desviaciones de consumo</span>
                  <p className="mt-2">
                    Detecta sobreconsumo de diésel y desviaciones del contenido de asfalto
                    (AC30) frente al diseño esperado.
                  </p>
                </div>

                <div className="rounded-xl border border-white/10 bg-white/5 p-4">
                  <span className="font-medium text-amber-300">Impacto directo en costo</span>
                  <p className="mt-2">
                    Convierte variaciones operativas en información accionable para reducir
                    pérdidas ocultas y mejorar decisiones.
                  </p>
                </div>
              </div>
            </div>

            <div className="flex flex-col justify-between rounded-2xl border border-cyan-400/20 bg-cyan-400/5 p-8">
              <div>
                <h3 className="mb-5 text-2xl font-semibold text-white">
                  Impacto del caso real
                </h3>

                <p className="mb-6 leading-8 text-slate-300">
                  La operación pasó de un modelo reactivo a un modelo proactivo, con
                  mayor control, trazabilidad y capacidad de decisión en tiempo real.
                </p>

                <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
                  <div className="rounded-xl border border-white/10 bg-white/5 p-5">
                    <div className="mb-1 text-sm text-cyan-300">Control</div>
                    <div className="font-semibold text-white">Mayor visibilidad operativa</div>
                  </div>
                  <div className="rounded-xl border border-white/10 bg-white/5 p-5">
                    <div className="mb-1 text-sm text-cyan-300">Trazabilidad</div>
                    <div className="font-semibold text-white">Validación inmediata</div>
                  </div>
                  <div className="rounded-xl border border-white/10 bg-white/5 p-5">
                    <div className="mb-1 text-sm text-cyan-300">Eficiencia</div>
                    <div className="font-semibold text-white">Menos tiempo de análisis</div>
                  </div>
                  <div className="rounded-xl border border-white/10 bg-white/5 p-5">
                    <div className="mb-1 text-sm text-cyan-300">Decisión</div>
                    <div className="font-semibold text-white">Operación más proactiva</div>
                  </div>
                </div>
              </div>

              <div className="mt-8 rounded-2xl border border-cyan-400/20 bg-slate-900/70 p-6">
                <p className="text-xl font-semibold leading-relaxed text-white md:text-2xl">
                  “SAS SmartPlant no es un concepto. Es un sistema validado en operación real
                  que detecta pérdidas que antes no eran visibles.”
                </p>
              </div>
            </div>
          </div>

          <div className="rounded-3xl border border-white/10 bg-white/5 p-8 text-center md:p-10">
            <h3 className="mb-4 text-2xl font-bold text-white md:text-3xl">
              De la teoría a la operación real
            </h3>
            <p className="mx-auto mb-8 max-w-3xl text-lg leading-8 text-slate-300">
              Descubre cómo SAS SmartPlant convierte datos operativos en alertas,
              control y decisiones en tiempo real.
            </p>

            <div className="flex flex-col items-center justify-center gap-4 sm:flex-row">
              <a
                href="https://sas-smartplant-nfhbmqb39yeacmngdyan4i.streamlit.app/"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center justify-center rounded-xl bg-cyan-500 px-6 py-3 font-semibold text-white transition hover:bg-cyan-400"
              >
                Ver demo real
              </a>

              <a
                href="#contacto"
                className="inline-flex items-center justify-center rounded-xl border border-white/15 bg-white/5 px-6 py-3 font-semibold text-white transition hover:bg-white/10"
              >
                Solicitar presentación
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* FEATURES */}
      <section className="mx-auto max-w-7xl px-6 py-16 lg:px-8">
        <div className="max-w-3xl">
          <h2 className="text-3xl font-bold tracking-tight">Lo que resuelve SAS SmartPlant</h2>
          <p className="mt-3 text-slate-400">
            Diseñado para transformar datos operativos dispersos en control real, alertas útiles y decisiones más rápidas.
          </p>
        </div>

        <div className="mt-10 grid gap-6 md:grid-cols-2 xl:grid-cols-4">
          {features.map((feature) => (
            <div
              key={feature.title}
              className="rounded-3xl border border-white/10 bg-white/[0.03] p-6 shadow-lg shadow-black/20"
            >
              <div className="text-lg font-semibold text-white">{feature.title}</div>
              <p className="mt-3 text-sm leading-7 text-slate-400">{feature.text}</p>
            </div>
          ))}
        </div>
      </section>

      {/* CÓMO FUNCIONA */}
      <section className="border-y border-white/10 bg-white/[0.02]">
        <div className="mx-auto grid max-w-7xl gap-10 px-6 py-16 lg:grid-cols-2 lg:px-8">
          <div>
            <h2 className="text-3xl font-bold tracking-tight">Cómo funciona</h2>
            <p className="mt-3 text-slate-400">
              Captura → analiza → detecta → alerta → decide.
            </p>
            <div className="mt-8 space-y-4">
              {steps.map((step, index) => (
                <div
                  key={step}
                  className="flex items-start gap-4 rounded-2xl border border-white/10 bg-slate-900/60 p-4"
                >
                  <div className="flex h-10 w-10 items-center justify-center rounded-full bg-sky-500/20 text-sm font-bold text-sky-300">
                    {index + 1}
                  </div>
                  <div className="pt-1 text-slate-200">{step}</div>
                </div>
              ))}
            </div>
          </div>

          <div>
            <h2 className="text-3xl font-bold tracking-tight">Valor para el cliente</h2>
            <div className="mt-8 grid gap-4 sm:grid-cols-2">
              {[
                "Menos pérdidas ocultas",
                "Mayor trazabilidad operativa",
                "Mejor conciliación de inventarios",
                "Más visibilidad para gerencia",
                "Alertas antes de que el problema crezca",
                "Base para escalar con IA",
              ].map((item) => (
                <div
                  key={item}
                  className="rounded-2xl border border-emerald-400/15 bg-emerald-500/5 p-4 text-sm text-emerald-200"
                >
                  {item}
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* CTA DEMO */}
      <section className="mx-auto max-w-6xl px-6 py-20 text-center lg:px-8">
        <h2 className="text-3xl font-bold tracking-tight text-white sm:text-4xl">
          Mira el sistema en acción
        </h2>
        <p className="mt-4 text-lg text-slate-400">
          Visualiza cómo SAS SmartPlant detecta pérdidas, interpreta desviaciones y ayuda a tomar decisiones en tiempo real.
        </p>
        <div className="mt-8">
          <a
            href="https://sas-smartplant-nfhbmqb39yeacmngdyan4i.streamlit.app/"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex rounded-2xl bg-emerald-500 px-8 py-4 text-lg font-semibold text-white shadow-lg shadow-emerald-500/20 transition hover:bg-emerald-400"
          >
            Ver demo completo
          </a>
        </div>
      </section>

      {/* CONTACTO */}
      <section className="mx-auto max-w-7xl px-6 py-16 lg:px-8" id="contacto">
        <div className="rounded-[32px] border border-white/10 bg-gradient-to-br from-sky-500/10 via-slate-900 to-emerald-500/10 p-8 lg:p-12">
          <div className="grid gap-10 lg:grid-cols-2 lg:items-center">
            <div>
              <h2 className="text-3xl font-bold tracking-tight">
                Empieza a detectar pérdidas hoy
              </h2>
              <p className="mt-4 max-w-2xl text-slate-300">
                Ideal para reuniones con aliados comerciales, clientes piloto e inversionistas interesados en tecnología aplicada a la operación industrial.
              </p>
            </div>

            <div className="rounded-3xl border border-white/10 bg-slate-950/70 p-6">
              <div className="space-y-4 text-sm text-slate-300">
                <div>
                  <div className="text-slate-500">Empresa</div>
                  <div className="mt-1 rounded-2xl border border-white/10 bg-white/5 px-4 py-3">
                    SAS SmartPlant
                  </div>
                </div>

                <div>
                  <div className="text-slate-500">Contacto</div>
                  <div className="mt-1 rounded-2xl border border-white/10 bg-white/5 px-4 py-3">
                    Gilberto Grimaldo
                  </div>
                </div>

                <div>
                  <div className="text-slate-500">Enfoque</div>
                  <div className="mt-1 rounded-2xl border border-white/10 bg-white/5 px-4 py-3">
                    Plantas de asfalto e industria pesada
                  </div>
                </div>
              </div>

              <a
                href="https://wa.me/50769818827"
                target="_blank"
                rel="noopener noreferrer"
                className="mt-6 block w-full rounded-2xl bg-sky-500 px-5 py-3 text-center text-sm font-semibold text-white transition hover:bg-sky-400"
              >
                Hablar por WhatsApp
              </a>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

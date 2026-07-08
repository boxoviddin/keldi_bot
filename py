<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keldi Bot</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body { 
            margin: 0; padding: 0; height: 100vh; overflow: hidden; 
            background: linear-gradient(135deg, #000428, #004e92, #411430, #000000);
            background-size: 400% 400%;
            animation: moveGradient 15s ease infinite;
            font-family: 'Segoe UI', sans-serif;
        }

        @keyframes moveGradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .glass-effect {
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .neon-glow-cyan {
            box-shadow: 0 0 15px #06b6d4, inset 0 0 5px #06b6d4;
            border: 1px solid #06b6d4;
        }

        .neon-glow-red {
            box-shadow: 0 0 15px #e11d48, inset 0 0 5px #e11d48;
            border: 1px solid #e11d48;
        }

        input::placeholder { color: rgba(255, 255, 255, 0.5); }
    </style>
</head>
<body class="text-white flex items-center justify-center">

    <div id="app" class="w-full max-w-sm p-6">
        
        <!-- Welcome Screen -->
        <div id="screen-welcome" class="text-center space-y-8 animate-in fade-in duration-700">
            <h1 class="text-5xl font-extrabold tracking-tighter text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-red-500 drop-shadow-[0_0_10px_rgba(255,255,255,0.5)]">
                Keldi Bot
            </h1>
            <p class="text-cyan-100 text-sm opacity-80">Neon tungi muhit sizni kutmoqda</p>
            <button onclick="showBooking()" class="w-full py-4 bg-transparent hover:bg-cyan-950 rounded-xl font-bold transition neon-glow-cyan uppercase tracking-widest text-cyan-300">
                Bron qilish
            </button>
        </div>

        <!-- Booking Screen -->
        <div id="screen-form" class="hidden w-full space-y-4 glass-effect p-6 rounded-2xl neon-glow-cyan">
            <h2 class="text-xl font-semibold text-center text-cyan-400 mb-4">Ma'lumotlarni kiriting</h2>
            <input type="text" id="ism" placeholder="Ismingiz" class="w-full p-3 bg-black/40 border border-cyan-800 rounded-lg outline-none focus:border-cyan-400 transition">
            <input type="text" id="familiya" placeholder="Familiyangiz" class="w-full p-3 bg-black/40 border border-cyan-800 rounded-lg outline-none focus:border-cyan-400 transition">
            <input type="time" id="time" class="w-full p-3 bg-black/40 border border-cyan-800 rounded-lg outline-none text-white focus:border-cyan-400 transition">
            <button onclick="submitBooking()" class="w-full py-3 bg-red-900/50 hover:bg-red-600 rounded-lg font-bold neon-glow-red transition uppercase border border-red-500 text-white">
                Tasdiqlash
            </button>
        </div>

        <!-- Success Screen -->
        <div id="screen-success" class="hidden text-center glass-effect p-8 rounded-3xl neon-glow-red">
            <h2 class="text-2xl font-bold text-red-400 mb-2">Qabul qilindi!</h2>
            <p id="msg-time" class="text-cyan-300"></p>
        </div>
    </div>

    <script>
        const tg = window.Telegram.WebApp;
        tg.expand();

        function showBooking() {
            document.getElementById('screen-welcome').classList.add('hidden');
            document.getElementById('screen-form').classList.remove('hidden');
        }

        function submitBooking() {
            const ism = document.getElementById('ism').value;
            const time = document.getElementById('time').value;

            if(!ism || !time) return alert("Barcha maydonlarni to'ldiring!");

            const data = {
                ism: ism,
                time: time,
                user_id: tg.initDataUnsafe.user?.id || "unknown"
            };

            tg.sendData(JSON.stringify(data));
            
            document.getElementById('screen-form').classList.add('hidden');
            document.getElementById('screen-success').classList.remove('hidden');
            document.getElementById('msg-time').innerText = `Kutib qolamiz: ${time}`;
        }
    </script>
</body>
</html>

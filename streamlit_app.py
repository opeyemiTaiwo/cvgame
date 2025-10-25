import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="Catch the Stars! 🌟",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit branding
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# The complete HTML game code with HIGH SCORE CHALLENGE and CELEBRATIONS
html_game = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catch the Stars!</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            cursor: none;
        }
        body {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background: linear-gradient(to bottom, #0f0c29, #302b63, #24243e);
            overflow: hidden;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        #gameContainer {
            position: relative;
            width: 100%;
            height: 100vh;
            background: linear-gradient(to bottom, #1a1a2e, #16213e);
            overflow: hidden;
        }
        #gameCanvas {
            width: 100%;
            height: 100%;
            display: block;
        }
        #startScreen, #gameOverScreen {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.9);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 100;
            text-align: center;
            padding: 20px;
        }
        .hidden {
            display: none !important;
        }
        h1 {
            font-size: 5em;
            background: linear-gradient(45deg, #00d4ff, #ff00ff, #ffff00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 30px;
            animation: rainbow 3s ease infinite;
        }
        @keyframes rainbow {
            0%, 100% { filter: hue-rotate(0deg); }
            50% { filter: hue-rotate(360deg); }
        }
        .instruction {
            font-size: 1.8em;
            margin: 15px 0;
            color: #fff;
        }
        .highlight {
            color: #00ff00;
            font-weight: bold;
            font-size: 1.2em;
        }
        .warning {
            color: #ff9900;
            font-size: 1.2em;
            font-weight: bold;
        }
        .startBtn {
            background: linear-gradient(45deg, #00d4ff, #ff00ff);
            border: none;
            color: white;
            font-size: 2.5em;
            padding: 25px 80px;
            margin: 40px;
            border-radius: 50px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        .startBtn:hover {
            transform: scale(1.1) !important;
        }
        #scoreBoard {
            position: absolute;
            top: 20px;
            left: 20px;
            background: rgba(0, 0, 0, 0.8);
            padding: 25px;
            border-radius: 20px;
            border: 4px solid #00d4ff;
            z-index: 50;
            font-size: 1.5em;
            min-width: 250px;
        }
        .scoreItem {
            margin: 8px 0;
            font-weight: bold;
            display: flex;
            justify-content: space-between;
        }
        .scoreValue {
            color: #00ff00;
            font-size: 1.2em;
        }
        .level { color: #ff9900 !important; }
        .missed { color: #ff0000 !important; }
        .highscore { color: #FFD700 !important; }
        #highScoreChallenge {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: linear-gradient(135deg, rgba(255, 215, 0, 0.95), rgba(255, 140, 0, 0.95));
            padding: 30px 60px;
            border-radius: 25px;
            border: 5px solid #FFD700;
            z-index: 45;
            text-align: center;
            box-shadow: 0 0 50px rgba(255, 215, 0, 0.8);
        }
        #highScoreChallenge h2 {
            font-size: 2.5em;
            color: white;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
            margin-bottom: 15px;
        }
        #highScoreChallenge .challengeScore {
            font-size: 4em;
            color: #fff;
            font-weight: bold;
            text-shadow: 4px 4px 8px rgba(0,0,0,0.7);
        }
        #comboDisplay {
            position: absolute;
            top: 120px;
            right: 30px;
            background: linear-gradient(45deg, #ff00ff, #ff0080);
            padding: 20px 40px;
            border-radius: 20px;
            font-size: 2.5em;
            font-weight: bold;
            color: white;
            z-index: 50;
            animation: comboAnim 0.5s ease;
        }
        @keyframes comboAnim {
            0% { transform: scale(0); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }
        #speedIndicator {
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(255, 0, 0, 0.8);
            padding: 15px 25px;
            border-radius: 15px;
            font-size: 1.2em;
            font-weight: bold;
            color: white;
            z-index: 50;
            border: 3px solid #ff0000;
        }
        #instructions {
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.8);
            padding: 20px 50px;
            border-radius: 20px;
            font-size: 1.4em;
            z-index: 50;
            color: #00ff00;
            border: 3px solid #00ff00;
        }
        .stat {
            margin: 10px 0;
            font-size: 1.3em;
        }
        #newHighScore {
            font-size: 2em;
            color: #FFD700;
            font-weight: bold;
            margin: 20px 0;
            animation: goldPulse 1s infinite;
        }
        @keyframes goldPulse {
            0%, 100% { 
                transform: scale(1); 
                text-shadow: 0 0 20px #FFD700;
            }
            50% { 
                transform: scale(1.1); 
                text-shadow: 0 0 40px #FFD700, 0 0 60px #FFD700;
            }
        }
        .highScoreDisplay {
            font-size: 1.5em;
            color: #FFD700;
            margin: 15px 0;
            text-shadow: 0 0 10px #FFD700;
        }
        #celebration {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 200;
        }
        .confetti {
            position: absolute;
            width: 10px;
            height: 10px;
            background: #FFD700;
            animation: confettiFall 3s linear;
        }
        @keyframes confettiFall {
            0% {
                transform: translateY(-100px) rotate(0deg);
                opacity: 1;
            }
            100% {
                transform: translateY(100vh) rotate(720deg);
                opacity: 0;
            }
        }
        #trophyBurst {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 15em;
            animation: trophyAnimation 2s ease-out;
            pointer-events: none;
            z-index: 250;
        }
        @keyframes trophyAnimation {
            0% {
                transform: translate(-50%, -50%) scale(0) rotate(-180deg);
                opacity: 0;
            }
            50% {
                transform: translate(-50%, -50%) scale(1.5) rotate(20deg);
                opacity: 1;
            }
            100% {
                transform: translate(-50%, -50%) scale(1) rotate(0deg);
                opacity: 1;
            }
        }
        .firework {
            position: absolute;
            width: 5px;
            height: 5px;
            border-radius: 50%;
            animation: fireworkExplosion 1s ease-out;
        }
        @keyframes fireworkExplosion {
            0% {
                transform: translate(0, 0);
                opacity: 1;
            }
            100% {
                transform: translate(var(--tx), var(--ty));
                opacity: 0;
            }
        }
    </style>
</head>
<body>
    <div id="gameContainer">
        <canvas id="gameCanvas"></canvas>
        <div id="celebration"></div>
        
        <div id="startScreen">
            <h1>🌟 CATCH THE STARS! 🌟</h1>
            <div class="highScoreDisplay">🏆 High Score: <span id="startHighScore">0</span></div>
            <p class="instruction">🖱️ Move your <span class="highlight">MOUSE</span> to catch stars!</p>
            <p class="instruction">⭐ Don't miss <span class="highlight">10 stars</span>!</p>
            <p class="instruction">🔥 Build <span class="highlight">COMBOS</span> for bonus!</p>
            <p class="instruction warning">⚡ Beat the HIGH SCORE to win!</p>
            <button class="startBtn" onclick="startGame()">▶ START!</button>
        </div>
        
        <div id="gameOverScreen" class="hidden">
            <h1>🎮 GAME OVER! 🎮</h1>
            <div id="newHighScore" class="hidden">🏆 NEW HIGH SCORE! 🏆</div>
            <div class="stat" id="finalScore"></div>
            <div class="stat highScoreDisplay">🏆 High Score: <span id="displayHighScore">0</span></div>
            <div class="stat" id="finalStars"></div>
            <div class="stat" id="finalCombo"></div>
            <button class="startBtn" onclick="restartGame()">🔄 PLAY AGAIN!</button>
        </div>
        
        <div id="scoreBoard" class="hidden">
            <div class="scoreItem">
                <span>Score:</span>
                <span class="scoreValue" id="score">0</span>
            </div>
            <div class="scoreItem">
                <span>🏆 Best:</span>
                <span class="scoreValue highscore" id="highScore">0</span>
            </div>
            <div class="scoreItem">
                <span>Level:</span>
                <span class="scoreValue level" id="level">1</span>
            </div>
            <div class="scoreItem">
                <span>Missed:</span>
                <span class="scoreValue missed" id="missed">0/10</span>
            </div>
        </div>
        
        <div id="highScoreChallenge" class="hidden">
            <h2>🏆 CAN YOU BEAT? 🏆</h2>
            <div class="challengeScore" id="challengeScore">0</div>
        </div>
        
        <div id="speedIndicator" class="hidden">
            ⚡ Speed: <span id="speedValue">100</span>%
        </div>
        
        <div id="comboDisplay" class="hidden">
            COMBO x<span id="combo">0</span>! 🔥
        </div>
        
        <div id="instructions" class="hidden">
            ⚡ Beat the high score! ⚡
        </div>
    </div>
    
    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);
        
        let gameRunning = false;
        let score = 0, combo = 0, maxCombo = 0, missed = 0, level = 1;
        let highScore = 0;
        let stars = [], particles = [];
        let basket = { x: 0, y: 0, size: 80 };
        let mouse = { x: 0, y: 0 };
        let spawnTimer = 0, gameSpeed = 1;
        let celebrationTriggered = false;
        
        const starColors = ['#FFD700', '#FFFF00', '#FF1493', '#FF69B4', '#00BFFF', '#00FF7F', '#DA70D6', '#FFA500', '#FF6347', '#7FFF00', '#FF00FF', '#00FFFF'];
        
        function loadHighScore() {
            const saved = localStorage.getItem('catchStarsHighScore');
            highScore = saved ? parseInt(saved) : 0;
            document.getElementById('highScore').textContent = highScore;
            document.getElementById('startHighScore').textContent = highScore;
            document.getElementById('displayHighScore').textContent = highScore;
            document.getElementById('challengeScore').textContent = highScore;
        }
        
        function saveHighScore() {
            if (score > highScore) {
                highScore = score;
                localStorage.setItem('catchStarsHighScore', highScore);
                return true;
            }
            return false;
        }
        
        function createConfetti() {
            const celebration = document.getElementById('celebration');
            const colors = ['#FFD700', '#FF6347', '#00FF7F', '#00BFFF', '#FF00FF', '#FFFF00'];
            
            for (let i = 0; i < 100; i++) {
                setTimeout(() => {
                    const confetti = document.createElement('div');
                    confetti.className = 'confetti';
                    confetti.style.left = Math.random() * 100 + '%';
                    confetti.style.background = colors[Math.floor(Math.random() * colors.length)];
                    confetti.style.animationDelay = Math.random() * 0.5 + 's';
                    celebration.appendChild(confetti);
                    
                    setTimeout(() => confetti.remove(), 3000);
                }, i * 30);
            }
        }
        
        function createTrophyBurst() {
            const trophy = document.createElement('div');
            trophy.id = 'trophyBurst';
            trophy.textContent = '🏆';
            document.getElementById('gameContainer').appendChild(trophy);
            
            setTimeout(() => trophy.remove(), 2000);
        }
        
        function createFireworks() {
            const celebration = document.getElementById('celebration');
            const colors = ['#FFD700', '#FF6347', '#00FF7F', '#00BFFF', '#FF00FF'];
            
            for (let i = 0; i < 5; i++) {
                setTimeout(() => {
                    const x = 20 + Math.random() * 60;
                    const y = 20 + Math.random() * 60;
                    
                    for (let j = 0; j < 30; j++) {
                        const firework = document.createElement('div');
                        firework.className = 'firework';
                        firework.style.left = x + '%';
                        firework.style.top = y + '%';
                        firework.style.background = colors[Math.floor(Math.random() * colors.length)];
                        
                        const angle = (j / 30) * Math.PI * 2;
                        const distance = 100 + Math.random() * 100;
                        firework.style.setProperty('--tx', Math.cos(angle) * distance + 'px');
                        firework.style.setProperty('--ty', Math.sin(angle) * distance + 'px');
                        
                        celebration.appendChild(firework);
                        setTimeout(() => firework.remove(), 1000);
                    }
                }, i * 500);
            }
        }
        
        function triggerCelebration() {
            if (celebrationTriggered) return;
            celebrationTriggered = true;
            
            createTrophyBurst();
            createConfetti();
            createFireworks();
            
            document.getElementById('highScoreChallenge').style.display = 'none';
        }
        
        loadHighScore();
        
        document.addEventListener('mousemove', (e) => {
            mouse.x = e.clientX;
            mouse.y = e.clientY;
        });
        
        document.addEventListener('touchmove', (e) => {
            e.preventDefault();
            const touch = e.touches[0];
            mouse.x = touch.clientX;
            mouse.y = touch.clientY;
        });
        
        class Star {
            constructor() {
                this.x = Math.random() * (canvas.width - 60) + 30;
                this.y = -50;
                this.size = 25 + Math.random() * 20;
                this.speed = (3 + Math.random() * 3) * gameSpeed;
                this.color = starColors[Math.floor(Math.random() * starColors.length)];
                this.rotation = 0;
                this.caught = false;
            }
            update() {
                if (!this.caught) {
                    this.y += this.speed;
                    this.rotation += 4;
                }
            }
            draw() {
                ctx.save();
                ctx.translate(this.x, this.y);
                ctx.rotate(this.rotation * Math.PI / 180);
                ctx.shadowBlur = 20;
                ctx.shadowColor = this.color;
                ctx.fillStyle = this.color;
                ctx.strokeStyle = 'white';
                ctx.lineWidth = 3;
                ctx.beginPath();
                for (let i = 0; i < 5; i++) {
                    const angle = (i * 4 * Math.PI / 5) - Math.PI / 2;
                    const x = Math.cos(angle) * this.size;
                    const y = Math.sin(angle) * this.size;
                    if (i === 0) ctx.moveTo(x, y);
                    else ctx.lineTo(x, y);
                }
                ctx.closePath();
                ctx.fill();
                ctx.stroke();
                ctx.fillStyle = 'white';
                ctx.beginPath();
                ctx.arc(0, 0, this.size / 3, 0, Math.PI * 2);
                ctx.fill();
                ctx.restore();
            }
            checkCatch() {
                const dx = this.x - basket.x;
                const dy = this.y - basket.y;
                return Math.sqrt(dx * dx + dy * dy) < basket.size / 2 + this.size;
            }
        }
        
        class Particle {
            constructor(x, y, color) {
                this.x = x;
                this.y = y;
                this.vx = (Math.random() - 0.5) * 10;
                this.vy = (Math.random() - 0.5) * 10 - 3;
                this.color = color;
                this.life = 60;
                this.size = 3 + Math.random() * 5;
            }
            update() {
                this.x += this.vx;
                this.y += this.vy;
                this.vy += 0.3;
                this.life--;
            }
            draw() {
                ctx.globalAlpha = this.life / 60;
                ctx.fillStyle = this.color;
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
                ctx.globalAlpha = 1;
            }
        }
        
        function drawBasket() {
            basket.x = mouse.x;
            basket.y = mouse.y;
            ctx.save();
            ctx.shadowBlur = 30;
            ctx.shadowColor = '#00d4ff';
            const gradient = ctx.createRadialGradient(basket.x, basket.y, 0, basket.x, basket.y, basket.size/2);
            gradient.addColorStop(0, '#00d4ff');
            gradient.addColorStop(1, '#0040ff');
            ctx.fillStyle = gradient;
            ctx.strokeStyle = 'white';
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.arc(basket.x, basket.y, basket.size / 2, 0, Math.PI * 2);
            ctx.fill();
            ctx.stroke();
            ctx.restore();
        }
        
        function explode(x, y, color) {
            for (let i = 0; i < 25; i++) {
                particles.push(new Particle(x, y, color));
            }
        }
        
        function updateUI() {
            document.getElementById('score').textContent = score;
            document.getElementById('level').textContent = level;
            document.getElementById('missed').textContent = missed + '/10';
            document.getElementById('speedValue').textContent = Math.round(gameSpeed * 100);
            document.getElementById('highScore').textContent = highScore;
            
            if (score > highScore && highScore > 0 && !celebrationTriggered) {
                triggerCelebration();
            }
            
            if (combo > 1) {
                document.getElementById('combo').textContent = combo;
                document.getElementById('comboDisplay').classList.remove('hidden');
            } else {
                document.getElementById('comboDisplay').classList.add('hidden');
            }
        }
        
        function gameLoop() {
            if (!gameRunning) return;
            ctx.fillStyle = 'rgba(26, 26, 46, 0.3)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            spawnTimer++;
            const spawnRate = Math.max(15, 45 - level * 4);
            const maxStarsOnScreen = Math.min(25, 8 + level * 2);
            
            if (spawnTimer > spawnRate) {
                if (stars.length < maxStarsOnScreen) {
                    stars.push(new Star());
                }
                spawnTimer = 0;
            }
            
            for (let i = stars.length - 1; i >= 0; i--) {
                const star = stars[i];
                star.update();
                star.draw();
                
                if (star.checkCatch() && !star.caught) {
                    star.caught = true;
                    score += 10 + combo * 5;
                    combo++;
                    maxCombo = Math.max(maxCombo, combo);
                    explode(star.x, star.y, star.color);
                    stars.splice(i, 1);
                    updateUI();
                    continue;
                }
                
                if (star.y > canvas.height + 50) {
                    missed++;
                    combo = 0;
                    stars.splice(i, 1);
                    updateUI();
                    
                    if (missed >= 10) {
                        endGame();
                        return;
                    }
                }
            }
            
            for (let i = particles.length - 1; i >= 0; i--) {
                particles[i].update();
                particles[i].draw();
                if (particles[i].life <= 0) particles.splice(i, 1);
            }
            
            drawBasket();
            
            const newLevel = Math.floor(score / 150) + 1;
            if (newLevel > level) {
                level = newLevel;
                gameSpeed = 1 + (level - 1) * 0.3;
                updateUI();
            }
            
            requestAnimationFrame(gameLoop);
        }
        
        function startGame() {
            document.getElementById('startScreen').classList.add('hidden');
            document.getElementById('scoreBoard').classList.remove('hidden');
            document.getElementById('speedIndicator').classList.remove('hidden');
            document.getElementById('instructions').classList.remove('hidden');
            
            if (highScore > 0) {
                document.getElementById('highScoreChallenge').classList.remove('hidden');
            }
            
            score = 0; combo = 0; maxCombo = 0; missed = 0; level = 1;
            gameSpeed = 1; stars = []; particles = []; spawnTimer = 0;
            celebrationTriggered = false;
            
            updateUI();
            gameRunning = true;
            gameLoop();
        }
        
        function endGame() {
            gameRunning = false;
            const isNewHighScore = saveHighScore();
            
            document.getElementById('finalScore').innerHTML = '🏆 Score: <span class="highlight">' + score + '</span>';
            document.getElementById('displayHighScore').textContent = highScore;
            document.getElementById('finalStars').innerHTML = '⭐ Caught: <span class="highlight">' + Math.floor(score / 10) + '</span>';
            document.getElementById('finalCombo').innerHTML = '🔥 Max Combo: <span class="highlight">x' + maxCombo + '</span>';
            
            if (isNewHighScore) {
                document.getElementById('newHighScore').classList.remove('hidden');
            } else {
                document.getElementById('newHighScore').classList.add('hidden');
            }
            
            document.getElementById('gameOverScreen').classList.remove('hidden');
            document.getElementById('highScoreChallenge').classList.add('hidden');
        }
        
        function restartGame() {
            document.getElementById('gameOverScreen').classList.add('hidden');
            document.getElementById('celebration').innerHTML = '';
            startGame();
        }
    </script>
</body>
</html>
"""

# Display the game
components.html(html_game, height=800, scrolling=False)

let timerInterval = null;
let seconds = 0;
let minutes = 0;

function startTimer() {
    try {
        if (!timerInterval) {
            timerInterval = setInterval(() => {
                seconds++;
                if (seconds >= 60) {
                    seconds = 0;
                    minutes++;
                }
                updateTimerDisplay();
            }, 1000);
        }
    } catch (error) {
        console.error('Error en startTimer:', error);
    }
}

function stopTimer() {
    try {
        if (timerInterval) {
            clearInterval(timerInterval);
            timerInterval = null;
        }
    } catch (error) {
        console.error('Error en stopTimer:', error);
    }
}

function resetTimer() {
    try {
        stopTimer();
        seconds = 0;
        minutes = 0;
        updateTimerDisplay();
    } catch (error) {
        console.error('Error en resetTimer:', error);
    }
}

function updateTimerDisplay() {
    try {
        const display = document.getElementById('timer-display');
        if (display) {
            const formattedTime = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
            display.textContent = formattedTime;
        }
    } catch (error) {
        console.error('Error en updateTimerDisplay:', error);
    }
}

const quotes = [
    "La educación es el arma más poderosa que puedes usar para cambiar el mundo.",
    "El conocimiento es poder, la información es libertad.",
    "Nunca dejes de aprender, porque la vida nunca deja de enseñar.",
    "La educación no es preparación para la vida; la educación es la vida misma.",
    "El futuro pertenece a aquellos que creen en la belleza de sus sueños."
];

let currentQuoteIndex = 0;

function rotateQuotes() {
    try {
        const quoteElement = document.querySelector('.rotating-text');
        if (quoteElement) {
            currentQuoteIndex = (currentQuoteIndex + 1) % quotes.length;
            quoteElement.style.opacity = '0';
            setTimeout(() => {
                quoteElement.textContent = quotes[currentQuoteIndex];
                quoteElement.style.opacity = '1';
            }, 300);
        }
    } catch (error) {
        console.error('Error en rotateQuotes:', error);
    }
}

function checkQuizAnswer(questionId, selectedOption, correctAnswer) {
    try {
        const resultDiv = document.getElementById(`result-${questionId}`);
        if (resultDiv) {
            if (selectedOption === correctAnswer) {
                resultDiv.className = 'quiz-result correct';
                resultDiv.textContent = '✅ ¡Correcto! Excelente trabajo.';
            } else {
                resultDiv.className = 'quiz-result incorrect';
                resultDiv.textContent = `❌ Incorrecto. La respuesta correcta es: ${correctAnswer}`;
            }
            resultDiv.style.display = 'block';
        }
    } catch (error) {
        console.error('Error en checkQuizAnswer:', error);
    }
}

function animateCards() {
    try {
        const cards = document.querySelectorAll('.card-materia, .info-card, .tool-card');
        if (cards.length > 0) {
            cards.forEach((card, index) => {
                card.style.animationDelay = `${index * 0.1}s`;
            });
        }
    } catch (error) {
        console.error('Error en animateCards:', error);
    }
}

function initWordSearch() {
    try {
        const grid = document.getElementById('word-search-grid');
        if (!grid) return;
        
        const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        const gridSize = 10;
        
        let gridHTML = '<div style="display: grid; grid-template-columns: repeat(10, 1fr); gap: 5px; max-width: 500px; margin: 0 auto;">';
        
        for (let i = 0; i < gridSize * gridSize; i++) {
            const randomLetter = letters[Math.floor(Math.random() * letters.length)];
            gridHTML += `<div class="word-search-cell" 
                         style="background: white; padding: 10px; text-align: center; border-radius: 5px; cursor: pointer; font-weight: bold;" 
                         onmouseover="this.style.background='#667eea'; this.style.color='white'" 
                         onmouseout="this.style.background='white'; this.style.color='black'">${randomLetter}</div>`;
        }
        
        gridHTML += '</div>';
        grid.innerHTML = gridHTML;
    } catch (error) {
        console.error('Error en initWordSearch:', error);
    }
}

function typeWriter(element, text, speed = 50) {
    try {
        if (!element) return;
        
        let i = 0;
        element.textContent = '';
        
        function type() {
            try {
                if (i < text.length) {
                    element.textContent += text.charAt(i);
                    i++;
                    setTimeout(type, speed);
                }
            } catch (error) {
                console.error('Error en type (typeWriter):', error);
            }
        }
        
        type();
    } catch (error) {
        console.error('Error en typeWriter:', error);
    }
}

function initTerminal() {
    try {
        const terminal = document.getElementById('terminal-content');
        if (!terminal) return;
        
        const commands = [
            { prompt: '$ ', command: 'echo "Hola Mundo"', output: 'Hola Mundo' },
            { prompt: '$ ', command: 'ls -la', output: 'index.html  style.css  script.js' },
            { prompt: '$ ', command: 'whoami', output: 'estudiante-smart-edu' }
        ];
        
        let html = '';
        commands.forEach(cmd => {
            html += `<div class="terminal-line">`;
            html += `<span class="terminal-prompt">${cmd.prompt}</span>`;
            html += `<span>${cmd.command}</span>`;
            html += `</div>`;
            html += `<div class="terminal-line">${cmd.output}</div>`;
        });
        
        terminal.innerHTML = html;
    } catch (error) {
        console.error('Error en initTerminal:', error);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    try {
        animateCards();
        
        if (document.querySelector('.rotating-text')) {
            setInterval(rotateQuotes, 5000);
        }
        
        initWordSearch();
        initTerminal();
        
        const links = document.querySelectorAll('a[href^="#"]');
        if (links.length > 0) {
            links.forEach(link => {
                link.addEventListener('click', function(e) {
                    e.preventDefault();
                    const targetId = this.getAttribute('href');
                    const target = document.querySelector(targetId);
                    if (target) {
                        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    }
                });
            });
        }
    } catch (error) {
        console.error('Error en DOMContentLoaded:', error);
    }
});

function startQuiz(quizId) {
    try {
        const quizElement = document.getElementById(quizId);
        if (quizElement) {
            quizElement.style.display = 'block';
        }
    } catch (error) {
        console.error('Error en startQuiz:', error);
    }
}

function submitQuiz(quizId) {
    try {
        const form = document.getElementById(quizId);
        if (!form) return;
        
        let score = 0;
        const answers = form.querySelectorAll('input[type="radio"]:checked');
        
        answers.forEach(answer => {
            if (answer.dataset.correct === 'true') {
                score++;
            }
        });
        
        const result = document.getElementById(`${quizId}-result`);
        if (result) {
            result.textContent = `🎯 ¡Obtuviste ${score} de ${answers.length} respuestas correctas!`;
            result.style.display = 'block';
        }
    } catch (error) {
        console.error('Error en submitQuiz:', error);
    }
}

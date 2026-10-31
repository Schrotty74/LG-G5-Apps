import QtQuick 2.4
import Eos.Window 0.1
WebOSWindow {
    id: win
    width: 1920; height: 1080
    windowType: "_WEBOS_WINDOW_TYPE_SCREENSAVER"
    appId: "com.webos.app.screensaver"
    title: "Screen Saver"
    visible: true
    color: "black"
    property int level: __TVWEB_LEVEL__
    property real t: Math.random() * 200
    Timer { interval: 100; running: true; repeat: true; onTriggered: { win.t += 0.1; scene.requestPaint() } }
    Canvas {
        id: scene
        anchors.fill: parent
        onPaint: {
            var c = getContext("2d"), w = width, h = height, t = win.t
            c.clearRect(0, 0, w, h)
            var phase = Math.floor(t / 45) % 4
            var colors = win.level ? ["#ca87a3", "#c3b26b", "#b66d3d", "#b1cbd5"] : ["#805268", "#776c3c", "#754729", "#607986"]
            for (var i = 0; i < 22; i++) {
                var x = (i * 193 + t * (8 + i % 5) + 40 * Math.sin(t * 0.17 + i)) % (w + 100) - 50
                var y = (i * 149 + t * (phase === 1 ? -5 : 12 + i % 5) + 100000) % h
                c.save(); c.translate(x, y); c.rotate(t * 0.25 + i)
                c.fillStyle = colors[phase]; c.strokeStyle = colors[phase]; c.lineWidth = 2
                if (phase === 0) {
                    // Spring: five petals around a small center.
                    for (var j = 0; j < 5; j++) {
                        var a = j * Math.PI * 2 / 5
                        c.beginPath(); c.arc(Math.cos(a) * 9, Math.sin(a) * 9, 7, 0, Math.PI * 2); c.fill()
                    }
                    c.fillStyle = win.level ? "#d6b875" : "#796841"
                    c.beginPath(); c.arc(0, 0, 4, 0, Math.PI * 2); c.fill()
                } else if (phase === 1) {
                    // Summer: small, pulsing fireflies.
                    c.globalAlpha = 0.35 + 0.5 * Math.abs(Math.sin(t * 0.8 + i))
                    c.beginPath(); c.arc(0, 0, 5 + 2 * Math.sin(t + i), 0, Math.PI * 2); c.fill()
                } else if (phase === 2) {
                    // Autumn: pointed leaves and their stem.
                    c.beginPath(); c.moveTo(0, -18); c.quadraticCurveTo(20, -4, 0, 15); c.quadraticCurveTo(-20, -4, 0, -18); c.fill()
                    c.strokeStyle = win.level ? "#e1a476" : "#a06b46"
                    c.beginPath(); c.moveTo(0, -14); c.lineTo(0, 20); c.stroke()
                } else {
                    // Winter: six-armed snowflakes.
                    for (var k = 0; k < 6; k++) {
                        var b = k * Math.PI / 3
                        c.beginPath(); c.moveTo(0, 0); c.lineTo(Math.cos(b) * 15, Math.sin(b) * 15); c.stroke()
                    }
                }
                c.restore()
            }
        }
    }
}

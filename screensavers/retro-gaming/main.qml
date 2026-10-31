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
    property real t: Math.random() * 500
    Timer { interval: 33; running: true; repeat: true; onTriggered: win.t += 0.033 }
    Repeater {
        model: 48
        Rectangle {
            width: index % 8 === 0 ? 4 : 2; height: width
            x: (index * 137 + win.t * (10 + index % 5)) % win.width
            y: (index * 239 + 45 * Math.sin(win.t * 0.06 + index)) % win.height
            color: win.level ? "#7191a4" : "#354c59"
            opacity: 0.35 + 0.4 * Math.abs(Math.sin(win.t * 0.8 + index))
        }
    }
    Repeater {
        model: 3
        Item {
            width: 100; height: 72
            x: (win.width - width) * (0.5 + 0.44 * Math.sin(win.t * (0.045 + index * 0.007) + index * 2.1))
            y: (win.height - height) * (0.5 + 0.42 * Math.cos(win.t * 0.039 + index * 1.9))
            property color hull: win.level ? "#59a6b6" : "#326172"
            Repeater {
                model: 35
                Rectangle {
                    property int col: index % 7
                    property int row: Math.floor(index / 7)
                    width: 12; height: 12; x: col * 12; y: row * 12
                    visible: (row === 0 && col === 3) || (row === 1 && col >= 2 && col <= 4) || (row === 2 && col >= 1 && col <= 5) || (row === 3) || (row === 4 && (col === 1 || col === 3 || col === 5))
                    color: (row === 2 && col === 3) ? (win.level ? "#dfb967" : "#826c3a") : parent.hull
                }
            }
        }
    }
}

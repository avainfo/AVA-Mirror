import LoadingAnimation from "./components/IntroAnimation.tsx";
import {useState} from "react";

function App() {
    const [showIntro, setShowIntro] = useState(true);
    return (
        <div style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            height: "100vh",
            width: "100vw",
            background: "#0a0a0a"
        }}>
            {showIntro && <LoadingAnimation onFinish={() => setShowIntro(false)}/>}
            {/*{!showIntro && <HomePage/>}*/}
        </div>
    );
}

export default App;

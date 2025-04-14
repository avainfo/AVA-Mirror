import {useEffect, useRef} from "react";
import "../style/LoadingAnimation.scss";

export default function IntroAnimation() {
    const videoRef = useRef<HTMLVideoElement>(null);

    const hasPaused1s = useRef(false);
    const hasPaused2s = useRef(false);
    const hasPaused3s = useRef(false);

    useEffect(() => {
        const video = videoRef.current;
        if (!video) return;

        video.play().catch((e) => {
            console.warn("Autoplay failed", e);
        });

        let frameId: number;

        const checkTime = () => {
            if (!video) return;

            const currentTime = video.currentTime;

            if (!hasPaused1s.current && currentTime >= 1 && currentTime < 1.1) {
                console.log("⏸ Pause 1s");
                hasPaused1s.current = true;
                video.pause();
                setTimeout(() => {
                    console.log("▶️ Resume 1s");
                    video.play();
                }, randomBetween(300, 750));
            } else if (!hasPaused2s.current && currentTime >= 2 && currentTime < 2.1) {
                console.log("⏸ Pause 2s");
                hasPaused2s.current = true;
                video.pause();
                setTimeout(() => {
                    console.log("▶️ Resume 2s");
                    video.play();
                }, randomBetween(100, 450));
            } else if (!hasPaused3s.current && currentTime >= 3 && currentTime < 3.1) {
                console.log("⏸ Pause 3s");
                hasPaused3s.current = true;
                video.pause();
                setTimeout(() => {
                    console.log("▶️ Resume 3s");
                    video.play();
                }, randomBetween(100, 450));
            }

            frameId = requestAnimationFrame(checkTime);
        };

        frameId = requestAnimationFrame(checkTime);

        return () => cancelAnimationFrame(frameId);
    }, []);

    const randomBetween = (min: number, max: number) => {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    };

    return (
        <div>
            <video
                ref={videoRef}
                src="/intro.mp4"
                muted
                loop={false}
                className="video-player"
            />
        </div>
    );
}

from core.engine import AimAssistEngine

def main():
    print("=== Aim Assist Module ===")
    engine = AimAssistEngine(persona="chaos-sniper", entropy=2.5)
    engine.calibrate()
    engine.engage()
    engine.shutdown()

if __name__ == "__main__":
    main()

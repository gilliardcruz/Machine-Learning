"""
Main entry point for the e-commerce sales forecasting application.
Provides CLI with commands for training, prediction, and web app.
"""

import sys
import argparse
import subprocess
from pathlib import Path

from src.logger import get_logger
from src.train import train_model
from src.predict import load_model, make_prediction

logger = get_logger(__name__)


def cmd_train(args) -> None:
    """Train the sales forecasting model."""
    logger.info("Starting model training...")
    try:
        train_model()
        logger.info("✅ Model training completed successfully!")
    except Exception as e:
        logger.error(f"❌ Training failed: {str(e)}")
        sys.exit(1)


def cmd_predict(args) -> None:
    """Make a sales prediction."""
    day = args.day
    month = args.month
    dow = args.dow

    # Validate inputs
    if not (1 <= day <= 31):
        logger.error("❌ Day must be between 1 and 31")
        sys.exit(1)
    if not (1 <= month <= 12):
        logger.error("❌ Month must be between 1 and 12")
        sys.exit(1)
    if not (0 <= dow <= 6):
        logger.error("❌ Day of week must be between 0 and 6")
        sys.exit(1)

    try:
        logger.info(f"Loading model...")
        model = load_model()

        logger.info(f"Making prediction for: {day:02d}/{month:02d} (Day of week: {dow})")
        prediction = make_prediction(model, day, month, dow)

        days_mapping = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
                       4: "Friday", 5: "Saturday", 6: "Sunday"}
        day_name = days_mapping[dow]

        print("\n" + "="*50)
        print("📊 SALES FORECAST RESULT")
        print("="*50)
        print(f"Date: {day:02d}/{month:02d} ({day_name})")
        print(f"Predicted Sales: R$ {prediction:,.2f}")
        print("="*50 + "\n")

        logger.info(f"✅ Prediction completed: R$ {prediction:,.2f}")

    except FileNotFoundError as e:
        logger.error(f"❌ {str(e)}")
        logger.info("💡 Please run 'python main.py train' to train the model first.")
        sys.exit(1)
    except ValueError as e:
        logger.error(f"❌ Invalid input: {str(e)}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Prediction failed: {str(e)}")
        sys.exit(1)


def cmd_app(args) -> None:
    """Launch the Streamlit web application."""
    app_path = Path(__file__).parent / "app" / "app.py"

    if not app_path.exists():
        logger.error(f"❌ App file not found at {app_path}")
        sys.exit(1)

    logger.info("🚀 Launching Streamlit app...")
    try:
        subprocess.run(
            ["streamlit", "run", str(app_path)],
            check=True
        )
    except FileNotFoundError:
        logger.error("❌ Streamlit not found. Please install it: pip install streamlit")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ App failed to start: {str(e)}")
        sys.exit(1)


def main():
    """Main entry point with argparse CLI."""
    parser = argparse.ArgumentParser(
        description="📊 E-commerce Sales Forecasting - Previsão de Vendas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py train                                    # Train the model
  python main.py predict --day 15 --month 3 --dow 2     # Make a prediction
  python main.py app                                      # Launch web app
        """
    )

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.2.0"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    subparsers.required = True

    # Train command
    train_parser = subparsers.add_parser("train", help="Train the sales forecasting model")
    train_parser.set_defaults(func=cmd_train)

    # Predict command
    predict_parser = subparsers.add_parser("predict", help="Make a sales prediction")
    predict_parser.add_argument(
        "--day",
        type=int,
        required=True,
        help="Day of month (1-31)"
    )
    predict_parser.add_argument(
        "--month",
        type=int,
        required=True,
        help="Month (1-12)"
    )
    predict_parser.add_argument(
        "--dow",
        type=int,
        required=True,
        help="Day of week (0=Monday, 1=Tuesday, ..., 6=Sunday)"
    )
    predict_parser.set_defaults(func=cmd_predict)

    # App command
    app_parser = subparsers.add_parser("app", help="Launch the Streamlit web application")
    app_parser.set_defaults(func=cmd_app)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

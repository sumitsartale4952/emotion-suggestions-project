import os

def create_structure(base_path, structure):
    """
    Recursively create directories and files based on the provided structure.
    
    Parameters:
        base_path (str): The directory in which to create the structure.
        structure (dict): A nested dictionary representing the file structure.
                          - Keys are file or directory names.
                          - If the value is None, it represents a file.
                          - If the value is a dict, it represents a directory.
    """
    for name, content in structure.items():
        current_path = os.path.join(base_path, name)
        if content is None:
            # It's a file; create an empty file.
            with open(current_path, "w") as f:
                f.write("")  # You can add template text here if desired.
            print(f"Created file: {current_path}")
        elif isinstance(content, dict):
            # It's a directory; create the directory.
            os.makedirs(current_path, exist_ok=True)
            print(f"Created directory: {current_path}")
            # Recursively create its content.
            create_structure(current_path, content)
        else:
            # In case of an unexpected type, skip.
            pass

if __name__ == "__main__":
    project_structure = {
        "README.md": None,
        "requirements.txt": None,
        ".gitignore": None,
        "app": {
            "__init__.py": None,
            "main.py": None,
            "ser": {
                "__init__.py": None,
                "audio_preprocessing.py": None,
                "feature_extraction.py": None,
                "model_training.py": None,
                "emotion_classifier.py": None,
                "models": {
                    "model.h5": None,
                    "model_metadata.json": None
                }
            },
            "suggestions": {
                "__init__.py": None,
                "activity_mapping.py": None,
                "recommendation_engine.py": None,
                "data": {
                    "music_data.csv": None,
                    "games_data.csv": None,
                    "user_preferences.json": None
                }
            },
            "utils": {
                "__init__.py": None,
                "audio_utils.py": None,
                "logging_utils.py": None,
                "api_utils.py": None
            },
            "tests": {
                "__init__.py": None,
                "test_ser.py": None,
                "test_suggestions.py": None,
                "test_utils.py": None
            }
        },
        "data": {
            "raw_audio": {},
            "processed_audio": {},
            "datasets": {}
        },
        "notebooks": {
            "ser_exploration.ipynb": None,
            "suggestions_exploration.ipynb": None,
            "data_preprocessing.ipynb": None
        },
        "docs": {
            "design_docs.md": None,
            "api_docs.md": None,
            "user_guide.md": None
        },
        "scripts": {
            "download_data.sh": None,
            "train_model.sh": None,
            "deploy.sh": None
        },
        "deployment": {
            "Dockerfile": None,
            "docker-compose.yml": None,
            "nginx.conf": None
        }
    }

    base_folder = "emotion-suggestions-project"
    os.makedirs(base_folder, exist_ok=True)
    create_structure(base_folder, project_structure)
    print("Project structure created successfully.")

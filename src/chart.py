import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Đọc file CSV
df = pd.read_csv('result.csv')

# Bảng ánh xạ từ các biến thể tên công nghệ về tên chuẩn
technology_mapping = {
    # Ngôn ngữ lập trình
    'bash': 'Bash/Shell',
    'bash/shell scripting': 'Bash/Shell',
    'shell script': 'Bash/Shell',
    'c': 'C/C++',
    'c++': 'C/C++',
    'c# .net': 'C#',
    'go': 'Golang',
    'javascript': 'JavaScript',
    'JS': 'JavaScript',
    'powershell': 'PowerShell',
    'python': 'Python',
    'tcl': 'Tcl',
    'typescript': 'TypeScript',
    
    # ===== Front-end =====
    # Frameworks và thư viện
    'angular': 'Angular',
    'angular cli': 'Angular',
    'angular js': 'Angular',
    'angular material': 'Angular',
    'angularjs': 'Angular',
    'ngrx': 'Angular',
    'ngx-charts': 'Angular',
    
    # React ecosystem
    'react': 'React',
    'reactjs': 'React',
    'reactjs': 'React',
    'react.js': 'React',
    'react context': 'React',
    'react hook form': 'React',
    'react query': 'React',
    'react router': 'React',
    'redux': 'React',
    'redux toolkit': 'React',
    'remixjs': 'React',
    'saga': 'React',
    'zustand': 'React',
    
    # Vue ecosystem
    'vue': 'Vue.js',
    'vue.js': 'Vue.js',
    'vuejs': 'Vue.js',
    'vuejs': 'Vue.js',
    'vue router': 'Vue.js',
    'vuex': 'Vue.js',
    'pinia': 'Vue.js',
    'nuxtjs': 'Vue.js',
    'nuxtjs': 'Vue.js',
    
    # CSS frameworks and utilities
    'bootstrap': 'Bootstrap',
    'tailwind css': 'Tailwind CSS',
    'tailwind css': 'Tailwind CSS',
    'tailwindcss': 'Tailwind CSS',
    'tailwindcss': 'Tailwind CSS',
    'tailwind': 'Tailwind CSS',
    'sass': 'Sass/SCSS',
    'scss': 'Sass/SCSS',
    'sass': 'Sass/SCSS',
    'less': 'LESS',
    'css': 'HTML/CSS',
    'css3': 'HTML/CSS',
    
    # HTML
    'html': 'HTML/CSS',
    'html5': 'HTML/CSS',
    'html/css': 'HTML/CSS',
    'pug': 'HTML/CSS',
    
    # UI libraries
    'ant design': 'Ant Design',
    'shadcn': 'ShadCN',
    
    # Utility libraries
    'jquery': 'jQuery',
    'jquery': 'jQuery',
    'axios': 'Axios',
    'fetch': 'Fetch API',
    'fetch api': 'Fetch API',
    'recharts': 'Recharts',
    'swiper': 'Swiper',
    'fancybox': 'Fancybox',
    
    # Build tools and bundlers
    'webpack': 'Webpack',
    'vite': 'Vite',
    'gulp': 'Gulp',
    
    # Development tools
    'eslint': 'ESLint',
    'prettier': 'Prettier',
    'chrome devtools': 'Chrome DevTools',
    
    # Testing
    'chai': 'Chai',
    'enzyme': 'Enzyme',
    
    # Others
    'es6': 'ES6',
    'context api': 'Context API',
    'cors': 'CORS',
    'sessionstorage': 'SessionStorage',
    'mvvm': 'MVVM',
    'mapkit': 'MapKit',
    'lvgl': 'LVGL',
    'sketch': 'Sketch',
    'bricks': 'Bricks',

    # ====== Back-end =====
    # .NET ecosystem
    '.net': '.NET',
    '.net 4+': '.NET',
    '.net 8.0': '.NET',
    '.net core': '.NET',
    '.net framework': '.NET',
    'dotnet': '.NET',
    'asp': 'ASP.NET',
    'asp.net': 'ASP.NET',
    'asp.net core': 'ASP.NET',
    'asp.net mvc': 'ASP.NET',
    'asp.net mvc 4+': 'ASP.NET',
    'asp.net core': 'ASP.NET',
    '.net mvc': 'ASP.NET',
    'mvc': 'MVC Pattern',
    'mvc 6': 'MVC Pattern',
    'ef core': 'Entity Framework',
    'wcf service': 'WCF',
    
    # Node.js ecosystem
    'node': 'Node.js',
    'node.js': 'Node.js',
    'nodejs': 'Node.js',
    'express': 'Express.js',
    'express.js': 'Express.js',
    'expressjs': 'Express.js',
    'actionhero': 'ActionHero',
    'adonisjs': 'AdonisJS',
    'nest': 'NestJS',
    'nestjs': 'NestJS',
    'nestjs': 'NestJS',
    'sails': 'Sails.js',
    'socket.io': 'Socket.IO',
    'nodemailer': 'Nodemailer',
    
    # Python ecosystem
    'django': 'Django',
    'flask': 'Flask',
    'flask-restful': 'Flask',
    'fastapi': 'FastAPI',
    'celery': 'Celery',
    'cherrypy': 'CherryPy',
    'gunicorn': 'Gunicorn',
    'uvicorn': 'Uvicorn',
    
    # Java ecosystem
    'spring': 'Spring',
    'spring boot': 'Spring Boot',
    'spring framework': 'Spring',
    'spring security': 'Spring',
    'hibernate': 'Hibernate',
    'jpos': 'jPOS',
    
    # PHP ecosystem
    'laravel': 'Laravel',
    'laravel reverb': 'Laravel',
    'lavarel': 'Laravel',
    'phpunit': 'PHPUnit',
    
    # Go ecosystem
    'gin': 'Gin',
    
    # Ruby ecosystem
    'rubocop': 'Rubocop',
    
    # API & Protocols
    'api': 'API',
    'graphql': 'GraphQL',
    'graphql apollo': 'GraphQL',
    'grpc': 'gRPC',
    'http': 'HTTP',
    'kamailio': 'Kamailio',
    'rest': 'REST API',
    'rest api': 'REST API',
    'restful api': 'REST API',
    'restful apis': 'REST API',
    'restful api': 'REST API',
    'openapi': 'OpenAPI',
    'sip protocol': 'SIP Protocol',
    'swagger': 'Swagger',
    'web api': 'Web API',
    'webrtc': 'WebRTC',
    'webhooks': 'Webhooks',
    'websocket': 'WebSocket',
    'websocket': 'WebSocket',
    'webservice': 'WebService',
    
    # Authentication & Security
    'bcrypt': 'Bcrypt',
    'jwt': 'JWT',
    'oauth': 'OAuth',
    'oauth2': 'OAuth2',
    'oauth2.0': 'OAuth2',
    
    # Architecture & Patterns
    'micro-services': 'Microservices',
    'middleware': 'Middleware',
    'orm': 'ORM',
    'orm framework': 'ORM',
    'typeorm': 'TypeORM',
    'rxjs': 'RxJS',
    
    # Web Servers & Infrastructure
    'nginx': 'Nginx',
    'server': 'Server',
    'socket': 'Socket',
    'pusher': 'Pusher',

    # Database
    'mysql': 'MySQL',
    'mysql workbench': 'MySQL',
    'mysql': 'MySQL',
    
    'postgresql': 'PostgreSQL',
    'postgre': 'PostgreSQL',
    'postgres': 'PostgreSQL',
    'postgressql': 'PostgreSQL',
    'pgvector': 'PostgreSQL',
    
    'mssql': 'SQL Server',
    'ms.sql': 'SQL Server',
    'sql server': 'SQL Server',
    
    'oracle': 'Oracle',
    'oracle database': 'Oracle',
    'oracle data integrator': 'Oracle',
    
    'sqlite': 'SQLite',
    'sql developer': 'SQL Developer',
    'sqlalchemy': 'SQLAlchemy',
    
    # NoSQL databases
    'mongodb': 'MongoDB',
    'moongodb': 'MongoDB',
    'nosql': 'NoSQL',
    'redis': 'Redis',
    'dynamodb': 'DynamoDB',
    'firebase': 'Firebase',
    'neo4j': 'Neo4j',
    
    # Search engines
    'elasticsearch': 'Elasticsearch',
    'elastic search': 'Elasticsearch',
    'elastic': 'Elasticsearch',
    
    # Vector databases
    'pinecone': 'Pinecone',
    
    # Data analytics
    'google bigquery': 'Google BigQuery',
    'looker': 'Looker',
    'metabase': 'Metabase',
    
    # Storage solutions
    'minio': 'MinIO',
    'rds': 'Amazon RDS',
    'questdb': 'QuestDB',
    
    # Generic terms
    'database': 'Database',

    # Deep Learning Frameworks
    'pytorch': 'PyTorch',
    'tensorflow': 'TensorFlow',
    'tensorflow lite': 'TensorFlow Lite',
    'tensorrt': 'TensorRT',
    'keras': 'Keras',
    'onnx': 'ONNX',
    
    # Natural Language Processing
    'nltk': 'NLTK',
    'spacy': 'SpaCy',
    'gensim': 'Gensim',
    'bert': 'BERT',
    'roberta': 'RoBERTa',
    'hugging face': 'Hugging Face',
    'huggingface': 'Hugging Face',
    'languagetool': 'LanguageTool',
    'gector': 'GECToR',
    
    # Large Language Models
    'llm': 'LLMs',
    'llms': 'LLMs',
    'langchain': 'LangChain',
    'langflow': 'Langflow',
    'langgraph': 'LangGraph',
    'llama': 'LLaMA',
    'llama index': 'Llama Index',
    'llamalindex': 'Llama Index',
    'openai': 'OpenAI',
    'openal': 'OpenAI',
    'openai api': 'OpenAI API',
    'openai gpt-40': 'OpenAI GPT-4o',
    'openai gpt-4o': 'OpenAI GPT-4o',
    'openai gpt api': 'OpenAI API',
    'gemini': 'Gemini',
    'gemini api': 'Gemini API',
    'google generative ai sdk': 'Google Generative AI SDK',
    'grok': 'Grok',
    'ollama': 'Ollama',
    'vllm': 'vLLM',
    'dify.ai': 'Dify.ai',
    'mojo ai': 'Mojo AI',
    'mojo ai agentic framework': 'Mojo AI',
    'dialogflow cx': 'Dialogflow CX',
    'rasa': 'Rasa',
    
    # Computer Vision
    'opencv': 'OpenCV',
    'yolo': 'YOLO',
    'resnet': 'ResNet',
    'detectron2': 'Detectron2',
    'mediapipe': 'Mediapipe',
    'albumentations': 'Albumentations',
    'stable diffusion': 'Stable Diffusion',
    'midjourney': 'Midjourney',
    
    # OCR
    'ocr': 'OCR',
    'tesseract': 'Tesseract',
    'tessent': 'Tesseract',
    'pytesseract': 'Pytesseract',
    'paddleocr': 'PaddleOCR',
    
    # Data Processing and Visualization
    'numpy': 'NumPy',
    'pandas': 'Pandas',
    'matplotlib': 'Matplotlib',
    'seaborn': 'Seaborn',
    'plotly': 'Plotly',
    'pillow': 'Pillow',
    'beautifulsoup': 'BeautifulSoup',
    'pyspark': 'PySpark',
    'dask': 'Dask',
    'networkx': 'NetworkX',
    'tableau': 'Tableau',
    'jupyter': 'Jupyter Notebook',
    'jupyter notebook': 'Jupyter Notebook',
    
    # ML Tools and Libraries
    'scikit learn': 'Scikit-learn',
    'scikit-learn': 'Scikit-learn',
    'xgboost': 'XGBoost',
    'lightgbm': 'LightGBM',
    'faiss': 'FAISS',
    'ml': 'Machine Learning',
    'machine learning': 'Machine Learning',
    
    # Text-to-Speech and Speech Processing
    'tts': 'TTS',
    
    # Security and Privacy
    'palisade': 'PALISADE',
    'concrete ml': 'Concrete ML',
    
    # Hardware Acceleration
    'cuda': 'CUDA',
    'triton': 'Triton',
    
    # Others
    'canva al': 'Canva AI',
    'adcreative.ai': 'Adcreative.ai',
    'talk2data': 'Talk2Data',
    'cvxpy': 'CVXPY',
    'nemo': 'Nemo',

    # AWS
    'aws': 'AWS',
    'amazon web service': 'AWS',
    'aws cloud': 'AWS',
    'amazon s3': 'AWS S3',
    's3': 'AWS S3',
    'ec2': 'AWS EC2',
    'aws sdk': 'AWS SDK',
    'aws cli': 'AWS CLI',
    'cloudwatch': 'AWS CloudWatch',
    'cloudformation': 'AWS CloudFormation',
    'aws ecs fargate': 'AWS ECS',
    'vpc': 'AWS VPC',
    'iam': 'AWS IAM',
    'glue': 'AWS Glue',
    
    # Azure
    'azure': 'Microsoft Azure',
    'microsoft azure': 'Microsoft Azure',
    'azure devops': 'Azure DevOps',
    'azure monitor': 'Azure Monitor',
    'azure security center': 'Azure Security Center',
    'microsoft entra id': 'Microsoft Entra ID',
    'microsoft intune': 'Microsoft Intune',
    
    # Google Cloud
    'gcp': 'Google Cloud',
    'google cloud': 'Google Cloud',
    
    # Other cloud providers
    'digitalocean': 'DigitalOcean',
    'alibaba cloud': 'Alibaba Cloud',
    'heroku': 'Heroku',
    'netlify': 'Netlify',
    'vercel': 'Vercel',
    'railway': 'Railway',
    'render': 'Render',
    
    # Containerization & Orchestration
    'docker': 'Docker',
    'dockerfile': 'Docker',
    'docker compose': 'Docker Compose',
    'kubernetes': 'Kubernetes',
    'k8s': 'Kubernetes',
    
    # CI/CD
    'ci/cd': 'CI/CD',
    'jenkins': 'Jenkins',
    'circleci': 'CircleCI',
    'nexus repository manager': 'Nexus Repository Manager',
    
    # Configuration Management & IaC
    'terraform': 'Terraform',
    'ansible': 'Ansible',
    
    # Monitoring & Logging
    'grafana': 'Grafana',
    'prometheus': 'Prometheus',
    'elk stack': 'ELK Stack',
    'splunk': 'Splunk',
    'new relic': 'New Relic',
    
    # Message Brokers
    'kafka': 'Apache Kafka',
    'apache kafka': 'Apache Kafka',
    'rabbitmq': 'RabbitMQ',
    'rabbitmq': 'RabbitMQ',
    
    # Data Processing
    'hadoop': 'Hadoop',
    'spark': 'Apache Spark',
    'spark core': 'Apache Spark',
    'spark sql': 'Apache Spark',
    'spark stream': 'Apache Spark',
    'databricks': 'Databricks',
    'databrick': 'Databricks',
    'adf': 'Azure Data Factory',
    'fabric': 'Microsoft Fabric',
    'nifi': 'Apache NiFi',
    'debezium': 'Debezium',
    'ibm datastage': 'IBM DataStage',
    
    # Operating Systems
    'ubuntu': 'Ubuntu',
    'centos': 'CentOS',
    'windows': 'Windows OS',
    'windows os': 'Windows OS',
    'windows autopilot': 'Windows Autopilot',
    
    # Virtualization
    'proxmox': 'Proxmox',
    'oracle vm': 'Oracle VM',
    'vpn': 'VPN',
    
    # Security
    'sentinel': 'Azure Sentinel',

    # React Native
    'react native': 'React Native',
    'react-native': 'React Native',
    'react native cli': 'React Native',
    
    # Flutter
    'flutter': 'Flutter',
    'dart': 'Flutter',  # Thêm Dart vì nó thường đi kèm với Flutter
    
    # Expo
    'expo': 'Expo',
    'expo cli': 'Expo',
    
    # Android
    'android': 'Android',
    'android sdk': 'Android',
    'android studio': 'Android',
    
    # iOS
    'ios': 'iOS',
    'swift': 'iOS',  # Thêm Swift vì nó thường đi kèm với iOS
    'objective-c': 'iOS',
    'xcode': 'iOS',
    
    # Xamarin
    'xamarin': 'Xamarin',
    'xamarin.android': 'Xamarin',
    'xamarin.forms': 'Xamarin',
    
    # Tools & Libraries
    'leakcanary': 'LeakCanary',
    
    # Capacitor/Ionic (thêm vào nếu cần)
    'capacitor': 'Capacitor/Ionic',
    'ionic': 'Capacitor/Ionic',

    # Unity
    'unity': 'Unity',
    'unity3d': 'Unity',
    'unity 3d': 'Unity',
    'unity engine': 'Unity',
    
    # Unreal
    'unreal engine': 'Unreal Engine',
    
    # Cocos
    'cocos': 'Cocos',
    'cocos2dx': 'Cocos',
    
    # DirectX
    'directx12': 'DirectX12',
    
    # OpenGL
    'opengl': 'OpenGL',
    'opengl es': 'OpenGL ES',
    'gles sl': 'OpenGL ES',
    
    # Vulkan
    'vulkan': 'Vulkan',
    
    # Others
    'libgdx': 'Libgdx',
    'phaser': 'Phaser',
    'roblox': 'Roblox',
    'xlua': 'Xlua',

    'arduino': 'Arduino',
    'arm': 'ARM',
    'arm 64 bit': 'ARM',
    'stm32': 'STM32',
    'stm32cubeide': 'STM32',
    'stm32g4': 'STM32',
    'esp32': 'ESP32',
    'raspberry pi': 'Raspberry Pi',
    'raspberry pi 5': 'Raspberry Pi',
    'fpga': 'FPGA',
    'jetson nano orin super': 'NVIDIA Jetson',
    'fieldy-nrf52840': 'Nordic nRF52',
    
    # RTOS & Embedded OS
    'freertos': 'FreeRTOS',
    'rtos': 'RTOS',
    'qnx': 'QNX',
    'qnx sensor framework': 'QNX',
    'embedded linux': 'Embedded Linux',
    
    # Protocols & Communication
    'can': 'CAN',
    'can protocol': 'CAN',
    'i2c': 'I2C',
    'spi': 'SPI',
    'uart': 'UART',
    'modbus': 'Modbus',
    'modbus 485': 'Modbus',
    'modbus rtu': 'Modbus',
    'mdb': 'MDB',
    'mqtt': 'MQTT',
    'opc-ua': 'OPC-UA',
    'tcp/ip': 'TCP/IP',
    'ip': 'TCP/IP',
    'ip scan': 'TCP/IP',
    'dhcp': 'DHCP',
    'dns': 'DNS',
    'vlan': 'VLAN',
    'switch': 'Networking',
    
    # Wireless Protocols
    'lora': 'LoRa',
    'lora mesh network': 'LoRa',
    'zigbee': 'Zigbee',
    'wi-fi': 'Wi-Fi',
    
    # Development Tools & SDKs
    'cubeide': 'STM32 CubeIDE',
    'cubemx': 'STM32 CubeMX',
    'platformio': 'PlatformIO',
    'platform io': 'PlatformIO',
    'esp-idf': 'ESP-IDF',
    'esp-matter sdk': 'ESP-Matter SDK',
    'qualcomm sdk': 'Qualcomm SDK',
    'segger rtt': 'SEGGER RTT',
    
    # IoT Platforms & Frameworks
    'tasmota': 'Tasmota',
    'thingboard': 'Thingsboard',
    'corelot': 'CorelIoT',
    'internet of things': 'IoT',
    'internet of things (iot)': 'IoT',
    'iot': 'IoT',
    
    # Automotive & Industrial
    'autosar': 'AUTOSAR',
    'ascet': 'ASCET',
    'labcar': 'Labcar',
    'plc': 'PLC',
    'tia portal': 'TIA Portal',
    
    # Network Simulation
    'eve-ng': 'EVE-NG',
    'gns3': 'GNS3',
    
    # Miscellaneous
    'c-4': 'C-4',
    'system verilog': 'System Verilog',

    'burp suite': 'Burp Suite',
    'burpsuite': 'Burp Suite',
    'burp suite professional': 'Burp Suite',
    'portswigger': 'PortSwigger',
    'dvwa': 'DVWA',
    'xss': 'XSS',
    'metasploit framework': 'Metasploit Framework',
    
    # Reverse Engineering
    'ida pro': 'IDA Pro',
    'ida pro': 'IDA Pro',
    'hopper': 'Hopper',
    'ghidra': 'Ghidra',
    'frida': 'Frida',
    
    # Unit Testing
    'jest': 'Jest',
    'junit': 'JUnit',
    'pytest': 'Pytest',
    'xunit': 'xUnit',
    'mocha': 'Mocha',
    'rspec': 'RSpec',
    'react testing library': 'React Testing Library',
    
    # Integration/E2E Testing
    'selenium': 'Selenium',
    'selenium grid': 'Selenium',
    'cypress': 'Cypress',
    'capybara': 'Capybara',
    'serenity': 'Serenity',
    
    # Performance Testing
    'jmeter': 'JMeter',
    
    # Code Quality
    'sonarqube': 'SonarQube',
    'checkmarx': 'Checkmarx',
    'php mess detector': 'PHP Mess Detector',
    'php codesniffer': 'PHP CodeSniffer',
    
    # Hardware/Chip Testing
    'drc/lvs check': 'DRC/LVS Check',
    'sva': 'SVA',
    'uvm': 'UVM',
    'vectorcast': 'VectorCast',
    
    # Apple
    'xcode': 'Xcode',
    'xnu': 'XNU',

    'bubble': 'Bubble.io',
    'bubble.io': 'Bubble.io',
    'forguncy': 'Forguncy',
    'glide': 'Glide',
    'nocodeb': 'NocoDB',
    'outsystems': 'OutSystems',
    'outsystems low-code platform': 'OutSystems',
    'softr': 'Softr',
    
    # Business Process Automation
    'rpa': 'RPA',
    'uipath': 'UiPath',
    
    # Integration & Workflow
    'integromat': 'Integromat',
    'n8n': 'n8n',
    'flowise': 'Flowise',
    'zapier': 'Zapier',
    
    # CMS & E-commerce
    'wordpress': 'WordPress',
    'woocommerce': 'WooCommerce',
    'woocomerce': 'WooCommerce',
    
    # ERP & CRM
    'erp': 'ERP',
    'odoo': 'Odoo',
    'misa': 'MISA',
    'vtigercrm': 'VtigerCRM',
    'wms': 'WMS',
    
    # Cloud Service Models
    'paas': 'PaaS',
    'saas': 'SaaS',

    'adobe xd': 'Adobe XD',
    'figma': 'Figma',
    'zeplin': 'Zeplin',
    'draw.io': 'Draw.io',
    'miro': 'Miro',
    'slack': 'Slack',
    'notion': 'Notion',
    'trello': 'Trello',
    'trello api': 'Trello API',
    'jira': 'Jira',
    'microsoft teams': 'Microsoft Teams',
    'zoom': 'Zoom',
    
    # Version Control & CI/CD
    'git': 'Git',
    'github': 'GitHub',
    'github actions': 'GitHub Actions',
    'github projects': 'GitHub Projects',
    'gitlab': 'GitLab',
    'svn': 'SVN',
    
    # IDEs & Code Editors
    'vs code': 'VS Code',
    'vscode': 'VS Code',
    'eclipse': 'Eclipse',
    'ide': 'IDE',
    
    # Microsoft Tools
    'microsoft 365': 'Microsoft 365',
    'microsoft excel': 'Microsoft Excel',
    'excel': 'Microsoft Excel',
    'microsoft power bi desktop': 'Power BI',
    'power bi': 'Power BI',
    'power bi dax': 'Power BI',
    'power bi service': 'Power BI',
    'microsoft power platform': 'Microsoft Power Platform',
    'power automate': 'Power Automate',
    'sharepoint': 'SharePoint',
    'microsoft promptflow': 'Microsoft Promptflow',
    'microsoft seal': 'Microsoft SEAL',
    
    # Google Tools
    'google apps script': 'Google Apps Script',
    'google colab': 'Google Colab',
    'google data studio': 'Google Data Studio',
    'google docs': 'Google Docs',
    'google maps': 'Google Maps',
    'google sheet': 'Google Sheets',
    'google sheets': 'Google Sheets',
    'google sheets api': 'Google Sheets API',
    'google workspace api': 'Google WorkSpace API',
    'looker studio': 'Looker Studio',
    
    # API Testing & Development
    'postman': 'Postman',
    'stripe': 'Stripe',
    'stripe checkout api': 'Stripe API',
    'vietqr api': 'VietQR API',
    
    # Databases & Data
    'phpmyadmin': 'phpMyAdmin',
    'prisma': 'Prisma ORM',
    'prisma orm': 'Prisma ORM',
    'erd': 'ERD',
    'power designer': 'Power Designer',
    'redash': 'Redash',
    'crystal reports': 'Crystal Reports',
    
    # Network & System Tools
    'cisco': 'Cisco',
    'cisco packet tracer': 'Cisco Packet Tracer',
    'wireshark': 'Wireshark',
    'winbox': 'Winbox',
    'xampp': 'XAMPP',
    'iis': 'IIS',
    
    # Development Paradigms & Methodology
    'agile/scrum': 'Agile/Scrum',
    'oop': 'OOP',
    'crud': 'CRUD',
    'collection': 'Collection',
    'exception': 'Exception',
    'forms': 'Forms',
    'localstorage': 'LocalStorage',
    'file management': 'File Management',
    
    # UI Frameworks & Libraries
    'maui': 'MAUI',
    'razor view': 'Razor View',
    'qml': 'QML',
    'qt': 'Qt',
    'zod': 'Zod',
    'babel': 'Babel',
    
    # CAD & Engineering Tools
    'auto cad': 'AutoCAD',
    'kicad': 'KiCad',
    'model sim': 'Model Sim',
    'tool cadence': 'Tool Cadence',
    'xcelium': 'Xcelium',
    'spatial x': 'Spatial X',
    
    # Video & Streaming
    'openvidu': 'OpenVidu',
    'livekit': 'LiveKit',
    
    # iOS Development Tools
    'class-dump': 'Class-dump',
    'dobby': 'Dobby',
    'fishhook': 'Fishhook',
    'hge': 'Hge',
    'litehook': 'Litehook',
    'lldb': 'LLDB',
    'mshook': 'MSHook',
    'otool': 'OTool',
    'theos': 'Theos',
    
    # Miscellaneous
    'cmake': 'CMake',
    'composer': 'Composer',
    'dal2': 'DAL2',
    'firefox': 'Firefox',
    'safari': 'Safari',
    'gradio': 'Gradio',
    'hl7': 'HL7',
    'htsc': 'HTSC',
    'log4j': 'Log4j',
    'pacs': 'PACS',
    'protocol buffers': 'Protocol Buffers',
    'rxlifecycle': 'RXLifecycle',
    'search tool': 'Search Tool',
    'smartbulk': 'SmartBulk',
    'way4': 'WAY4',

}
technology_mapping_lower = {k.lower(): v for k, v in technology_mapping.items()}

# Danh sách các ngôn ngữ lập trình cần thống kê
languages = [
    "Bash/Shell", 'C/C++', 'C#', 'Golang', 'Groovy',
    'Java', 'JavaScript', 'Kotlin', 'Lua', 'Objective-C',
    'Perl', 'PHP', 'Powershell', 'Python', 'Ruby','Swift', 'Tcl',
    'TypeScript', 'VBA', 'VB.NET', 'Verilog', 'yaml'
]

# Front-end
frontend_technologies = [
    "Angular", "React", "Vue.js", "Bootstrap", "Tailwind CSS", 
    "Sass/SCSS", "HTML", "HTML/CSS", "CSS", "jQuery", "Webpack", "Vite", 'Axios',
    'Recharts', 'Swiper', 'Fancybox', 'Gulp', 'EsLint', 'Prettier', 'Enzyme', 'Chai', "Shadcn"
]

# Back-end
backend_technologies = [
    '.NET', 'ASP.NET', 'Node.js', 'Express.js', 'NestJS', 
    'Django', 'Flask', 'FastAPI', 'Spring', 'Spring Boot',
    'Laravel', 'GraphQL', 'REST API', 'Microservices', 'WebSocket',
    'Gunicorn', 'Uvicorn', 'Nginx', 'ORM', 'TypeORM',
    'JWT', 'OAuth2'
]

# Danh sách các công nghệ database cần thống kê
database_technologies = [
    'MySQL', 'PostgreSQL', 'SQL Server', 'Oracle', 'SQLite', 
    'MongoDB', 'Redis', 'DynamoDB', 'Firebase', 'Neo4j',
    'Elasticsearch', 'Pinecone', 'Google BigQuery', 'MinIO',
    'Amazon RDS', 'QuestDB', 'NoSQL', 'SQL Developer', 'SQLAlchemy'
]

ai_ml_technologies = [
    'PyTorch', 'TensorFlow', 'Keras', 'Scikit-learn', 'NumPy', 'Pandas',
    'OpenCV', 'YOLO', 'Hugging Face', 'LLMs', 'OpenAI', 'Gemini', 
    'LangChain', 'Llama Index', 'Matplotlib', 'OCR', 'Tesseract',
    'Machine Learning', 'BERT', 'Stable Diffusion', 'NLTK', 'SpaCy',
    'XGBoost', 'Jupyter Notebook', 'Pillow', 'BeautifulSoup'
]

devops_cloud_technologies = [
    'AWS', 'AWS S3', 'AWS EC2', 'Microsoft Azure', 'Google Cloud', 
    'Docker', 'Docker Compose', 'Kubernetes', 'CI/CD', 'Jenkins',
    'Terraform', 'Ansible', 'Grafana', 'Prometheus', 'Apache Kafka',
    'RabbitMQ', 'Databricks', 'Azure Data Factory', 'Microsoft Fabric',
    'Hadoop', 'Apache Spark', 'Heroku', 'Vercel', 'Netlify', 'Railway',
    'Azure DevOps', 'Windows OS', 'Ubuntu', 'ELK Stack'
]

mobile_technologies = [
    'React Native', 'Flutter', 'Expo', 'Android', 'iOS', 
    'Xamarin', 'LeakCanary', 'Capacitor/Ionic'
]

game_dev_technologies = [
    'Unity', 'Unreal Engine', 'Cocos', 'DirectX12', 
    'OpenGL', 'OpenGL ES', 'Vulkan', 'Libgdx',
    'Phaser', 'Roblox', 'Xlua'
]

iot_embedded_technologies = [
    'Arduino', 'ARM', 'STM32', 'ESP32', 'Raspberry Pi', 'FPGA',
    'FreeRTOS', 'RTOS', 'QNX', 'Embedded Linux',
    'CAN', 'I2C', 'SPI', 'UART', 'Modbus', 'MQTT', 'OPC-UA', 'TCP/IP',
    'LoRa', 'Zigbee', 'Wi-Fi',
    'PlatformIO', 'ESP-IDF', 'STM32 CubeIDE', 'STM32 CubeMX',
    'IoT', 'PLC', 'AUTOSAR'
]

testing_security_technologies = [
    'Burp Suite', 'Metasploit Framework', 'XSS', 'IDA Pro', 'Ghidra', 'Frida',
    'Jest', 'JUnit', 'Pytest', 'Mocha', 'React Testing Library', 'RSpec',
    'Selenium', 'Cypress', 'Capybara', 'JMeter', 'SonarQube', 'Checkmarx',
    'PHP Mess Detector', 'PHP CodeSniffer', 'DRC/LVS Check', 'SVA', 'UVM',
    'Xcode', 'XNU', 'PortSwigger', 'DVWA', 'Hopper', 'xUnit', 'Serenity'
]

low_code_business_technologies = [
    'Bubble.io', 'OutSystems', 'WordPress', 'WooCommerce', 'Odoo',
    'UiPath', 'RPA', 'ERP', 'Zapier', 'MISA', 'VtigerCRM',
    'Glide', 'NocoDB', 'Integromat', 'Flowise', 'n8n',
    'Forguncy', 'Softr', 'PaaS', 'SaaS', 'WMS'
]

tools_misc_technologies = [
    'Figma', 'Adobe XD', 'Jira', 'Git', 'GitHub', 'VS Code',
    'Power BI', 'Microsoft Excel', 'Google Sheets', 'Postman',
    'Agile/Scrum', 'Draw.io', 'Slack', 'Notion', 'Trello',
    'Google Colab', 'phpMyAdmin', 'Prisma ORM', 'Wireshark',
    'Microsoft Teams', 'ERD', 'Cisco', 'Zoom', 'XAMPP', 'AutoCAD'
]

# Hàm để chuẩn hóa các công nghệ dựa trên bảng ánh xạ
def normalize_technology(tech_string):
    if not isinstance(tech_string, str):
        return []
    
    normalized_techs = []
    # Tách chuỗi thành các phần riêng biệt
    techs = [t.strip() for t in tech_string.split(',')]
    
    for tech in techs:
        # Chuyển về lowercase để so sánh không phân biệt hoa thường
        tech_lower = tech.lower()
        # Kiểm tra xem có trong bảng ánh xạ không
        if tech_lower in technology_mapping_lower:
            normalized_techs.append(technology_mapping_lower[tech_lower])
        else:
            normalized_techs.append(tech)
            
    return normalized_techs

# Hàm để đếm các từ khóa trong cột đã được chuẩn hóa
def count_normalized_keywords(df, keywords, column_name):
    counter = Counter()
    
    for tech_string in df[column_name].dropna():
        normalized_techs = normalize_technology(tech_string)
        dict = {}
        for tech in normalized_techs:
            for keyword in keywords:
                if keyword.lower() == tech.lower() and not dict.get(tech):
                    counter[keyword] += 1
                    dict[tech] = 1
                    break
    
    return counter

# Tạo biểu đồ
def create_chart(title, color, counts, save_name):
    plt.figure(figsize=(10, 8))
    bars = plt.barh(list(counts.keys()), list(counts.values()), color=color)
    plt.title(f'{title} phổ biến trong các công ty thực tập HK 242 HCMUT', fontsize=12)
    plt.xlabel('Số lượng công ty')
    plt.ylabel('Công cụ & Công nghệ bổ sung')
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    # Thêm số lượng cụ thể vào đầu mỗi cột
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 0.3, bar.get_y() + bar.get_height()/2, f'{width}',
                ha='left', va='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'chart/{save_name}.png')
    plt.close()

# Đếm ngôn ngữ và framework sau khi đã chuẩn hóa
language_counts = count_normalized_keywords(df, languages, 'Ngôn ngữ / Framework')
frontend_counts = count_normalized_keywords(df, frontend_technologies, 'Ngôn ngữ / Framework')
backend_counts = count_normalized_keywords(df, backend_technologies, 'Ngôn ngữ / Framework')
database_counts = count_normalized_keywords(df, database_technologies, 'Ngôn ngữ / Framework')
ai_ml_counts = count_normalized_keywords(df, ai_ml_technologies, 'Ngôn ngữ / Framework')
devops_cloud_counts = count_normalized_keywords(df, devops_cloud_technologies, 'Ngôn ngữ / Framework')
mobile_counts = count_normalized_keywords(df, mobile_technologies, 'Ngôn ngữ / Framework')
game_dev_counts = count_normalized_keywords(df, game_dev_technologies, 'Ngôn ngữ / Framework')
iot_embedded_counts = count_normalized_keywords(df, iot_embedded_technologies, 'Ngôn ngữ / Framework')
testing_security_counts = count_normalized_keywords(df, testing_security_technologies, 'Ngôn ngữ / Framework')
low_code_business_counts = count_normalized_keywords(df, low_code_business_technologies, 'Ngôn ngữ / Framework')
tools_misc_counts = count_normalized_keywords(df, tools_misc_technologies, 'Ngôn ngữ / Framework')


# Sắp xếp theo số lượng giảm dần
language_counts = dict(sorted(language_counts.items(), key=lambda x: x[1], reverse=False))
frontend_counts = dict(sorted(frontend_counts.items(), key=lambda x: x[1], reverse=False))
backend_counts = dict(sorted(backend_counts.items(), key=lambda x: x[1], reverse=False))
database_counts = dict(sorted(database_counts.items(), key=lambda x: x[1], reverse=False))
ai_ml_counts = dict(sorted(ai_ml_counts.items(), key=lambda x: x[1], reverse=False))
devops_cloud_counts = dict(sorted(devops_cloud_counts.items(), key=lambda x: x[1], reverse=False))
mobile_counts = dict(sorted(mobile_counts.items(), key=lambda x: x[1], reverse=False))
game_dev_counts = dict(sorted(game_dev_counts.items(), key=lambda x: x[1], reverse=False))
iot_embedded_counts = dict(sorted(iot_embedded_counts.items(), key=lambda x: x[1], reverse=False))
testing_security_counts = dict(sorted(testing_security_counts.items(), key=lambda x: x[1], reverse=False))
low_code_business_counts = dict(sorted(low_code_business_counts.items(), key=lambda x: x[1], reverse=False))
tools_misc_counts = dict(sorted(tools_misc_counts.items(), key=lambda x: x[1], reverse=False))

# Tạo biểu đồ ngang cho ngôn ngữ
create_chart('Ngôn ngữ lập trình', 'skyblue', language_counts, 'languages_chart')

# Tạo biểu đồ ngang cho Front-end
create_chart('Front-end library and framework', 'skyblue', frontend_counts, 'front-end_chart')

# Tạo biểu đồ ngang cho backend
create_chart('Backend Technologies', 'lightblue', backend_counts, 'backend_chart')

# Tạo biểu đồ ngang cho database
create_chart('Database Technologies', 'lightcoral', database_counts, 'database_chart')

# Tạo biểu đồ ngang cho AI/ML
create_chart('AI/ML Technologies', 'lightgreen', ai_ml_counts, 'ai_ml_chart')

# Tạo biểu đồ ngang cho DevOps/Cloud
create_chart('DevOps/Cloud Technologies', 'lightsalmon', devops_cloud_counts, 'devops_cloud_chart')

# Tạo biểu đồ ngang cho Mobile
create_chart('Mobile Development Technologies', 'mediumpurple', mobile_counts, 'mobile_chart')

# Tạo biểu đồ ngang cho Game Development
create_chart('Game Development Technologies', 'gold', game_dev_counts, 'game_dev_chart')

# Tạo biểu đồ ngang cho IoT/Embedded
create_chart('IoT/Embedded Technologies', 'aquamarine', iot_embedded_counts, 'iot_embedded_chart')

# Tạo biểu đồ ngang cho Testing/Security
create_chart('Testing/Security Technologies', 'orchid', testing_security_counts, 'testing_security_chart')

# Tạo biểu đồ ngang cho Low-Code/No-Code & Business Tools
create_chart('Low-Code/No-Code & Business Tools','paleturquoise', low_code_business_counts,'low_code_business_chart')

# Tạo biểu đồ ngang cho Tools & Misc Technologies
create_chart('Tools & Misc Technologies', 'plum', tools_misc_counts, 'tools_misc_chart')



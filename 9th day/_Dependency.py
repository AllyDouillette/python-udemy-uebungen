
dependencies = {
    "express": "^4.18.2",
    "jsonwebtoken": "^9.0.2",
    "prisma": "^5.9.1",
    "@prisma/client": "^5.9.1",
    "mermaid": "^10.8.0",
    "bcrypt": "^5.1.1",
    "dotenv": "^16.4.5",
    "cors": "^2.8.5",
    "eslint": "^8.56.0",
    "eslint-config-standard": "^17.1.0",
    "eslint-plugin-import": "^2.29.1",
    "eslint-plugin-n": "^16.6.2",
    "eslint-plugin-promise": "^6.1.1",
    "eslint-plugin-react": "^7.33.2",
    "lorem-ipsum": "^2.0.8",
    "morgan": "^1.10.0",
    "nodemon": "^3.0.3",
    "prettier": "^3.2.5",
    "unique-username-generator": "^1.3.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "xlsx": "^0.18.5",
    "@types/react": "^18.2.37",
    "@types/react-dom": "^18.2.15",
    "@vitejs/plugin-react": "^4.2.0",
    "eslint": "^8.53.0",
    "eslint-plugin-react": "^7.33.2",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.4",
    "vite": "^5.0.0"
}

def getVersionDescription (version):
    versionSpecification = ""
    versionNum = version
    if version[0] == "^":
        versionSpecification = "or future minor/patch versions"
        versionNum = version[1:]
    
    if version[0] == "~":
        versionSpecification = "or patch version variants"
        versionNum = version[1:]
    
    return " ".join([versionNum, versionSpecification])

def generateNPMLink (packagename):
    if packagename[0] == "@":
        packagename = packagename[1:]
        
    return "https://www.npmjs.com/package/"+packagename

def printDependencies (dict):
    for dependencyName in dict:
        versionNum = dict[dependencyName]
        name = dependencyName
        print(name, " – ", (getVersionDescription(versionNum)), " – ", generateNPMLink(dependencyName) )

printDependencies(dependencies)
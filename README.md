# Demo App - CI/CD Pipeline with AWS Elastic Beanstalk

A learning project demonstrating continuous integration and deployment using GitHub Actions and AWS Elastic Beanstalk.

## Project Structure

- `application.py` - Flask web application
- `test_app.py` - Unit tests
- `requirements.txt` - Python dependencies
- `.github/workflows/deploy.yml` - CI/CD workflow
- `.ebextensions/` - Elastic Beanstalk configuration

## Local Setup

1. **Clone or navigate to the project:**
   ```bash
   cd demo-app-second
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run locally:**
   ```bash
   python application.py
   ```
   Visit `http://localhost:5000/` and `http://localhost:5000/health`

5. **Run tests:**
   ```bash
   pytest test_app.py -v
   ```

## AWS Setup for Deployment

### 1. Create AWS Resources
- Create an Elastic Beanstalk application named `my-demo-app`
- Create an environment named `demo-env` in region `us-east-1`
- Choose Python 3.11 platform

### 2. Configure GitHub Secrets
Add these to your GitHub repository settings (Settings → Secrets and variables → Actions):
- `AWS_ACCESS_KEY_ID` - Your AWS access key
- `AWS_SECRET_ACCESS_KEY` - Your AWS secret key

### 3. Deploy
Push to the `main` branch to trigger:
1. **Test stage** - Runs pytest automatically
2. **Deploy stage** - Deploys to Elastic Beanstalk if tests pass

## Learning Points

✅ **CI/CD Pipeline** - GitHub Actions workflow  
✅ **Automated Testing** - pytest runs before deployment  
✅ **Infrastructure as Code** - Beanstalk configuration  
✅ **Secrets Management** - Using GitHub secrets for AWS credentials  
✅ **Deployment Automation** - One push = auto-test + auto-deploy  

## Next Steps to Learn More

1. Add environment-specific configuration
2. Implement health checks and monitoring
3. Add database integration
4. Use AWS RDS for persistent storage
5. Implement blue-green deployments

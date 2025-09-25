import { useState } from "react";
import "./FeaturesPage.css"; // keep styles separate

const FaqItem = ({ question, answer }) => {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <div className="faq-item">
      <button className="faq-question" onClick={() => setIsOpen(!isOpen)}>
        {question}
        <span>{isOpen ? "−" : "+"}</span>
      </button>
      <div className={`faq-answer ${isOpen ? "open" : ""}`}>
        <p>{answer}</p>
      </div>
    </div>
  );
};

function FeaturesPage() {
  const [activeTab, setActiveTab] = useState("doctors");

  const doctorFeatures = [
    { title: "Digital Prescription Creation", description: "Generate, sign, and send secure digital prescriptions in seconds, eliminating paperwork and reducing errors.", icon: "📋" },
    { title: "Patient Medication History", description: "Access a patient's complete prescription history instantly, allowing for more informed clinical decisions.", icon: "📚" },
    { title: "Refill Management", description: "Approve or deny prescription refill requests from pharmacists with a single click, saving valuable time.", icon: "🔄" },
    { title: "Prescription Templates", description: "Create and save templates for commonly prescribed medications to speed up your workflow.", icon: "📝" },
    { title: "Real-time Notifications", description: "Receive instant alerts when a prescription has been viewed and dispensed by the pharmacist.", icon: "🔔" },
    { title: "Secure Patient Database", description: "Manage your patient records with bank-level security and access them from anywhere, anytime.", icon: "🛡️" }
  ];

  const pharmacistFeatures = [
    { title: "Instant Prescription Receipt", description: "Receive digital prescriptions from doctors instantly, reducing wait times and transcription errors.", icon: "📥" },
    { title: "Automated Inventory Management", description: "Your inventory is automatically updated when a prescription is dispensed, helping you track stock levels.", icon: "📦" },
    { title: "Supplier Integration", description: "Directly manage orders with your suppliers and get alerts for low-stock items.", icon: "🚚" },
    { title: "Dispensing Logs & History", description: "Maintain a clear, digital log of all dispensed medications for easy auditing and record-keeping.", icon: "🗄️" },
    { title: "Refill Request System", description: "Send electronic refill requests to doctors for patient prescriptions that are running low.", icon: "📨" },
    { title: "Patient Profile Management", description: "Keep a comprehensive profile for each patient, including allergies and past medications.", icon: "👤" }
  ];

  // New patient features
  const patientFeatures = [
    { title: "Personal Medication Tracker", description: "Track all your medications and receive reminders for doses and refills.", icon: "💊" },
    { title: "Secure Health Records", description: "Access your prescription history and medical records securely anytime, anywhere.", icon: "🗂️" },
    { title: "Direct Communication with Doctors", description: "Message your healthcare provider directly for questions or prescription requests.", icon: "💬" },
    { title: "Pharmacy Locator", description: "Find nearby pharmacies and check availability of prescribed medications.", icon: "📍" },
    { title: "Refill Requests", description: "Send refill requests to your doctor digitally without waiting in queues.", icon: "🔄" },
    { title: "Treatment Insights", description: "Receive personalized insights and tips to improve adherence and health outcomes.", icon: "📊" }
  ];

  const faqs = [
    { q: "Is my patient data secure on this platform?", a: "Absolutely. We use end-to-end encryption and comply with all relevant healthcare data protection standards to ensure your data is always safe and confidential." },
    { q: "How much does the Pharma Project cost?", a: "We offer various subscription plans tailored to the needs of individual practitioners and large clinics. Please visit our pricing page for more details." },
    { q: "Can this platform integrate with my existing clinic software?", a: "We are actively working on integrations with popular clinic and pharmacy management systems. Please contact our support team to discuss your specific needs." },
    { q: "Is there a mobile app available?", a: "Yes, the Pharma Project is available as a fully-featured mobile application on both iOS and Android, allowing you to manage your work on the go." }
  ];

  return (
    <div className="features-container">
      <div className="features-hero">
        <h1>Tools Built for Modern Healthcare</h1>
        <p>
          Powerful, intuitive features designed to streamline your workflow and
          enhance patient care.
        </p>
      </div>

      <div className="section">
        <div className="tabs-container">
          <button
            className={`tab-button ${activeTab === "doctors" ? "active" : ""}`}
            onClick={() => setActiveTab("doctors")}
          >
            For Doctors
          </button>
          <button
            className={`tab-button ${activeTab === "pharmacists" ? "active" : ""}`}
            onClick={() => setActiveTab("pharmacists")}
          >
            For Pharmacists
          </button>
          <button
            className={`tab-button ${activeTab === "patients" ? "active" : ""}`}
            onClick={() => setActiveTab("patients")}
          >
            For Patients
          </button>
        </div>

        {activeTab === "doctors" && (
          <div className="features-grid">
            {doctorFeatures.map((f) => (
              <div key={f.title} className="feature-item-card">
                <div className="feature-icon">{f.icon}</div>
                <h3>{f.title}</h3>
                <p>{f.description}</p>
              </div>
            ))}
          </div>
        )}

        {activeTab === "pharmacists" && (
          <div className="features-grid">
            {pharmacistFeatures.map((f) => (
              <div key={f.title} className="feature-item-card">
                <div className="feature-icon">{f.icon}</div>
                <h3>{f.title}</h3>
                <p>{f.description}</p>
              </div>
            ))}
          </div>
        )}

        {activeTab === "patients" && (
          <div className="features-grid">
            {patientFeatures.map((f) => (
              <div key={f.title} className="feature-item-card">
                <div className="feature-icon">{f.icon}</div>
                <h3>{f.title}</h3>
                <p>{f.description}</p>
              </div>
            ))}
          </div>
        )}
      </div>

      <div className="shared-features-section section">
        <h2 className="section-title">Collaborate with Confidence</h2>
        <p className="section-subtitle">
          Features that bridge the gap and foster seamless teamwork.
        </p>
        <div className="features-grid">
          <div className="feature-item-card">
            <div className="feature-icon">💬</div>
            <h3>Secure Direct Messaging</h3>
            <p>
              Communicate directly and securely with other professionals to
              clarify prescription details or discuss patient care.
            </p>
          </div>
          <div className="feature-item-card">
            <div className="feature-icon">📊</div>
            <h3>Analytics & Reporting</h3>
            <p>
              Access insightful dashboards to track prescription volumes,
              dispensing rates, and inventory trends.
            </p>
          </div>
          <div className="feature-item-card">
            <div className="feature-icon">🌐</div>
            <h3>Unified Patient Profiles</h3>
            <p>
              View a shared, comprehensive patient profile that provides a
              holistic view of their medication history.
            </p>
          </div>
        </div>
      </div>

      <div className="faq-section section">
        <h2 className="section-title">Frequently Asked Questions</h2>
        <div className="faq-container">
          {faqs.map((faq) => (
            <FaqItem key={faq.q} question={faq.q} answer={faq.a} />
          ))}
        </div>
      </div>

      <div className="cta-section section">
        <h2 className="section-title">Ready to Upgrade Your Practice?</h2>
        <p className="section-subtitle">
          Join thousands of professionals who are streamlining their workflow
          and improving patient care with Pharma Project.
        </p>
        <a href="/signup" className="cta-button">
          Sign Up for Free
        </a>
      </div>
    </div>
  );
}

export default FeaturesPage;

import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import "../styles/Login.css";

const initialFormState = { email: "", password: "" };

export default function Login() {
  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const roleFromURL = params.get("role"); // doctor / pharmacist / patient

  const [role, setRole] = useState(roleFromURL || "doctor");
  const [formData, setFormData] = useState(initialFormState);
  const [isLoading, setIsLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  // Reset form when role changes
  useEffect(() => {
    setFormData(initialFormState);
    setMessage("");
  }, [role]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setIsLoading(true);
    setMessage("");

    // Fake API delay
    setTimeout(() => {
      setIsLoading(false);
      setMessage(`${role} login successful!`);
    }, 1500);
  };

  const sidebarContent = {
    doctor: {
      title: "For Medical Professionals",
      text: "Access patient records, manage prescriptions, and collaborate securely.",
    },
    pharmacist: {
      title: "For Pharmacy Experts",
      text: "Manage inventory, process prescriptions, and ensure patient care.",
    },
    patient: {
      title: "For Patients",
      text: "View your health records, book appointments, and consult with doctors safely.",
    },
  };

  return (
    <div className={`login-container role-${role}`}>
      <div className="login-wrapper">
        {/* Sidebar */}
        <div className="login-sidebar">
          <h2>{sidebarContent[role].title}</h2>
          <p>{sidebarContent[role].text}</p>
        </div>

        {/* Form */}
        <div className="login-panel">
          <div className="login-header">
            <h2>
              {role === "doctor"
                ? "Doctor Login"
                : role === "pharmacist"
                ? "Pharmacist Login"
                : "Patient Login"}
            </h2>
            <p>Welcome back! Please enter your credentials.</p>
          </div>

          <form className="login-form" onSubmit={handleSubmit}>
            {/* Show dropdown only if user didn’t come from modal */}
            {!roleFromURL && (
              <select
                className="login-select"
                value={role}
                onChange={(e) => setRole(e.target.value)}
              >
                <option value="doctor">Login as Doctor</option>
                <option value="pharmacist">Login as Pharmacist</option>
                <option value="patient">Login as Patient</option>
              </select>
            )}

            {/* Email */}
            <div className="login-group">
              <span className="login-icon">📧</span>
              <input
                className="login-input"
                type="email"
                name="email"
                placeholder="Email Address"
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>

            {/* Password */}
            <div className="login-group">
              <span className="login-icon">🔒</span>
              <input
                className="login-input"
                type={showPassword ? "text" : "password"}
                name="password"
                placeholder="Password"
                value={formData.password}
                onChange={handleChange}
                required
              />
              <span
                className="login-toggle"
                onClick={() => setShowPassword(!showPassword)}
              >
                {showPassword ? (
                  // Eye-off icon
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="25"
                    height="25"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 
                      0-11-8-11-8a18.45 18.45 0 0 1 
                      5.06-5.94M9.9 4.24A9.12 9.12 0 
                      0 1 12 4c7 0 11 8 11 8a18.5 
                      18.5 0 0 1-2.16 3.19m-6.72-1.07a3 
                      3 0 1 1-4.24-4.24"></path>
                    <line x1="1" y1="1" x2="23" y2="23"></line>
                  </svg>
                ) : (
                  // Eye icon
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="25"
                    height="25"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <path d="M1 12s4-8 11-8 11 8 11 
                      8-4 8-11 8-11-8-11-8z"></path>
                    <circle cx="12" cy="12" r="3"></circle>
                  </svg>
                )}
              </span>
            </div>

            {/* Submit Button */}
            <button type="submit" className="login-btn2" disabled={isLoading}>
              {isLoading ? "Logging In..." : "Login"}
            </button>
          </form>

          {/* Success/Error Messages */}
          {message && <p className="login-message">{message}</p>}

          {/* Links */}
          <div className="login-links">
            <a href={`/${role}-forgot-password`}>Forgot Password?</a>
            <span className="login-separator">·</span>
            <a href="/signup">Create an Account</a>
          </div>
        </div>
      </div>
    </div>
  );
}

import React, { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import "../styles/Login.css";

const initialFormState = { email: "", password: "" };

export default function Login() {
  const location = useLocation();
  const navigate = useNavigate(); // ✅ needed for redirect

  const params = new URLSearchParams(location.search);
  const roleFromURL = params.get("role");

  const [role, setRole] = useState(roleFromURL || "doctor");
  const [formData, setFormData] = useState(initialFormState);
  const [isLoading, setIsLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [showPassword, setShowPassword] = useState(false);

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

    // ⏳ Simulating API call
    setTimeout(() => {
      setIsLoading(false);
      setMessage(`Login successful! Redirecting...`);

      // 🎯 Redirect to dashboard
      navigate("/dashboard");   // <<— ONLY THIS LINE NEEDED
    }, 1200);
  };

  return (
    <div className={`login-container role-${role}`}>
      <div className="login-wrapper">

        {/* Sidebar */}
        <div className="login-sidebar">
          <h2>
            {role === "doctor"
              ? "For Medical Professionals"
              : role === "pharmacist"
              ? "For Pharmacy Experts"
              : "For Patients"}
          </h2>
          <p>Secure access to your healthcare portal.</p>
        </div>

        {/* Login Panel */}
        <div className="login-panel">
          <div className="login-header">
            <h2>
              {role === "doctor"
                ? "Doctor Login"
                : role === "pharmacist"
                ? "Pharmacist Login"
                : "Patient Login"}
            </h2>
            <p>Please enter your credentials.</p>
          </div>

          <form className="login-form" onSubmit={handleSubmit}>
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
                {showPassword ? "🙈" : "👁️"}
              </span>
            </div>

            <button type="submit" className="login-btn2" disabled={isLoading}>
              {isLoading ? "Logging In..." : "Login"}
            </button>
          </form>

          {message && <p className="login-message">{message}</p>}

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

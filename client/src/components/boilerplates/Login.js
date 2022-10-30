import "../../styles/login.css";
import { Link, useHistory } from "react-router-dom";
import { React, useState } from "react";
import { Button, Spinner } from "react-bootstrap";
import ReCAPTCHA from "react-google-recaptcha";

import { useEffect } from "react";

function Login({ user, loginUser }) {
  const history = useHistory();

  const [forgotPwd, setforgotPwd] = useState(false);
  const changeState = () => {
    setforgotPwd(true);
  };

  const [LoginCaptchaCheck, setLoginCaptchaCheck] = useState(false);
  const LoginCaptchaOnChange = (value) => {
    console.log("Captcha value:", value);
    setLoginCaptchaCheck(true);
  };

  const [ForgotPwdCaptchaCheck, setForgotPwdCaptchaCheck] = useState(false);
  const ForgotPwdCaptchaOnChange = (value) => {
    console.log("Captcha value:", value);
    setForgotPwdCaptchaCheck(true);
  };

  const [credentials, setCredentials] = useState({
    email: "",
    password: "",
  });

  useEffect(() => {
    user?.username && history.push("/collectionLogin");
  }, [history, user?.username]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCredentials({ ...credentials, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const { email, password } = credentials;
    loginUser({ email, password });
  };

  // window.localStorage.setItem("login",false);
  return forgotPwd === false ? (
    <div class="center form">
      <h1>Login</h1>
      <form onSubmit={handleSubmit} method="post">
        <div class="txt_field">
          <input
            type="email"
            name="email"
            id="email"
            onChange={handleChange}
            required
          />
          <span></span>
          <label for="email">Email</label>
        </div>
        <div class="txt_field">
          <input
            type="password"
            name="password"
            id="inputPwd"
            onChange={handleChange}
            required
          />
          <span></span>
          <label for="inputPwd">Password</label>
        </div>
        <div class="pass" onClick={changeState}>
          Forgot Password?
        </div>
        <ReCAPTCHA
          sitekey="6Ldrj30iAAAAADyAiEnHJkcZOv4E2UsyYK2ZQpvC"
          onChange={LoginCaptchaOnChange}
        />
        <input
          type="submit"
          disabled={!LoginCaptchaCheck}
          style={{ "border-radius": "30px;" }}
          value="Login"
        />
        <div class="signup_link">
          Not a member? <Link to="register">Signup</Link>
        </div>
      </form>
    </div>
  ) : (
    //--------forgot password form ---------
    <div class="center form" style={{ height: "400px" }}>
      <img
        src={require("../../images/forgot_password.png")}
        id="forgotIcon"
        alt=""
      ></img>
      <h1>Reset password</h1>
      <form action="forgotPassword" method="post">
        <div class="txt_field">
          <input
            type="email"
            name="email"
            id="email"
            placeholder="enter your email"
            required
          />
          <span></span>
        </div>
        <div style={{ marginTop: "-30px" }}>
          <ReCAPTCHA
            sitekey="6Ldrj30iAAAAADyAiEnHJkcZOv4E2UsyYK2ZQpvC"
            onChange={ForgotPwdCaptchaOnChange}
          />
        </div>
        <div>
          <Button
            type="submit"
            disabled={!ForgotPwdCaptchaCheck}
            variant="dark"
            style={{ width: "fit-content", "margin-left": "50px" }}
          >
            Reset password
          </Button>
          <Link to="/">
            <Button variant="dark" style={{ width: "fit-content" }}>
              Back
            </Button>
          </Link>
        </div>
      </form>
    </div>
  );
  //------------------------------------
}

export default Login;

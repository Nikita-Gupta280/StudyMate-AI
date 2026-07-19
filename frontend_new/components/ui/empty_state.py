import streamlit as st


def empty_state(
    title: str,
    message: str,
    icon: str = "📂",
    button_text: str = None,
    key: str = None,
):
    """
    Displays a reusable empty state.

    Returns
    -------
    bool

    Returns True if the button is clicked,
    otherwise False.
    """

    st.markdown(
        f"""
        <div style="
            border:1px solid #30363D;
            border-radius:18px;
            padding:50px;
            text-align:center;
            background:#161B22;
            margin:25px 0;
        ">

            <div style="
                font-size:70px;
                margin-bottom:15px;
            ">
                {icon}
            </div>

            <div style="
                font-size:28px;
                font-weight:bold;
                color:white;
            ">
                {title}
            </div>

            <div style="
                color:#A0A0A0;
                font-size:16px;
                margin-top:12px;
                line-height:1.6;
            ">
                {message}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if button_text:

        return st.button(
            button_text,
            key=key,
            type="primary",
            use_container_width=True,
        )

    return False
import streamlit as st


def section_header(
    title: str,
    subtitle: str = "",
    icon: str = "📌",
):
    """
    Reusable section header component.

    Parameters
    ----------
    title : str
        Section title

    subtitle : str
        Small description

    icon : str
        Emoji icon
    """

    st.markdown(
        f"""
        <div style="
            margin-top:10px;
            margin-bottom:20px;
        ">

            <div style="
                display:flex;
                align-items:center;
                gap:12px;
            ">

                <div style="
                    font-size:34px;
                ">
                    {icon}
                </div>

                <div>

                    <div style="
                        font-size:28px;
                        font-weight:700;
                        color:white;
                    ">
                        {title}
                    </div>

                    <div style="
                        color:#A0A0A0;
                        font-size:15px;
                        margin-top:2px;
                    ">
                        {subtitle}
                    </div>

                </div>

            </div>

            <hr style="
                border:none;
                border-top:1px solid #333;
                margin-top:18px;
            ">

        </div>
        """,
        unsafe_allow_html=True,
    )
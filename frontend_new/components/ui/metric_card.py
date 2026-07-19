import streamlit as st


def metric_card(
    title: str,
    value,
    icon: str = "📊",
    help_text: str | None = None,
):
    """
    Reusable metric card component.

    Parameters
    ----------
    title : str
        Metric title.

    value : str | int | float
        Metric value.

    icon : str
        Emoji icon.

    help_text : str | None
        Optional description.
    """

    st.markdown(
        f"""
        <div style="
            background:#1E1E1E;
            border:1px solid #333;
            border-radius:15px;
            padding:20px;
            text-align:center;
            height:150px;
            display:flex;
            flex-direction:column;
            justify-content:center;
        ">

            <div style="font-size:34px;">
                {icon}
            </div>

            <div style="
                color:#B0B0B0;
                font-size:15px;
                margin-top:8px;
            ">
                {title}
            </div>

            <div style="
                font-size:34px;
                font-weight:bold;
                margin-top:8px;
            ">
                {value}
            </div>

            {
                f'<div style="font-size:12px;color:#888;margin-top:8px;">{help_text}</div>'
                if help_text else ""
            }

        </div>
        """,
        unsafe_allow_html=True,
    )
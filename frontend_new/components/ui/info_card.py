import streamlit as st


def info_card(
    title: str,
    message: str,
    card_type: str = "info",
):
    """
    Reusable information card.

    Parameters
    ----------
    title : str
        Card title

    message : str
        Card message

    card_type : str

        info
        success
        warning
        error
    """

    styles = {

        "info": {
            "icon": "ℹ️",
            "color": "#2563EB",
            "background": "#1E3A8A",
        },

        "success": {
            "icon": "✅",
            "color": "#22C55E",
            "background": "#14532D",
        },

        "warning": {
            "icon": "⚠️",
            "color": "#F59E0B",
            "background": "#78350F",
        },

        "error": {
            "icon": "❌",
            "color": "#EF4444",
            "background": "#7F1D1D",
        },
    }

    style = styles.get(card_type, styles["info"])

    st.markdown(
        f"""
        <div style="
            background:{style['background']};
            border-left:6px solid {style['color']};
            border-radius:12px;
            padding:18px;
            margin:10px 0;
        ">

            <div style="
                font-size:22px;
                font-weight:bold;
                color:white;
            ">
                {style['icon']} {title}
            </div>

            <div style="
                margin-top:10px;
                color:#F3F4F6;
                font-size:15px;
                line-height:1.6;
            ">
                {message}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )
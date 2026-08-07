"""
Komara Agency — Bot WhatsApp Business
Auto-réponses et gestion client automatisée
Contact: +212 701-986219
"""

import json
import datetime
from typing import Dict, Optional

# ==================== CONFIGURATION ====================

BOT_CONFIG = {
    "agency_name": "Komara Agency",
    "slogan": "Vision. Impact. Excellence.",
    "whatsapp_number": "+212 701-986219",
    "timezone": "Africa/Conakry",
    "express_surcharge": 0.30,  # +30%
    "free_revisions": 2,
    "extra_revision_cost": 50000,  # GNF
    "payment_methods": ["Orange Money", "MTN Money", "Virement bancaire", "PayPal"],
}

# ==================== RÉPONSES AUTO ====================

CANNED_RESPONSES: Dict[str, Dict] = {
    "welcome": {
        "keywords": ["salut", "bonjour", "salam", "hello", "bonsoir", "slt", "cc"],
        "response": (
            "Salut ! 👋 Bienvenue chez Komara Agency 🇬🇳\n\n"
            "Je suis Ndine, ton créateur digital.\n"
            "Voici ce que je propose :\n\n"
            "1. 🎨 Logo pro\n"
            "2. 🖼️ Affiche & Flyer\n"
            "3. 📸 Retouche photo\n"
            "4. 🤖 Bots WhatsApp/Telegram\n"
            "5. ✨ Branding complet\n"
            "6. 🎬 Montage vidéo/Reels\n\n"
            "Tape le numéro du service qui t'intéresse 👇"
        ),
    },
    "logo": {
        "keywords": ["1", "logo", "logo pro", "logotype"],
        "response": (
            "🎨 *Logo Pro*\n\n"
            "Logo unique et sur mesure pour ta marque.\n\n"
            "💰 Tarif: 300k - 500k GNF\n"
            "⏱️ Délai: 48h-72h\n"
            "✅ 2 propositions + 2 révisions gratuites\n"
            "⚡ Express 24h: +30%\n\n"
            "Tape *commander* pour lancer ta demande 👇"
        ),
    },
    "affiche": {
        "keywords": ["2", "affiche", "flyer", "poster", "affiches"],
        "response": (
            "🖼️ *Affiche & Flyer*\n\n"
            "Design percutant pour tes événements et promos.\n\n"
            "💰 Tarif: 300k GNF\n"
            "⏱️ Délai: 24h-48h\n"
            "✅ 2 révisions gratuites\n"
            "⚡ Express 24h: +30%\n\n"
            "Tape *commander* pour lancer ta demande 👇"
        ),
    },
    "retouche": {
        "keywords": ["3", "retouche", "photo", "retouche photo", "edit photo"],
        "response": (
            "📸 *Retouche Photo*\n\n"
            "Retouche pro: fond, lumière, couleur, peau.\n"
            "Rendu naturel premium 8K.\n\n"
            "💰 Tarif: sur discussion\n"
            "⏱️ Délai: 24h-48h\n\n"
            "Envoie-moi ta photo et je te dis ce que je peux faire 👇"
        ),
    },
    "bots": {
        "keywords": ["4", "bot", "bots", "whatsapp bot", "telegram", "automatisation"],
        "response": (
            "🤖 *Bots WhatsApp / Telegram*\n\n"
            "Automatise ta communication client:\n"
            "- Messages de bienvenue\n"
            "- Réponses automatiques\n"
            "- Relances de paiement\n"
            "- Suivi de commandes\n\n"
            "💰 Tarif: sur devis\n"
            "Tape *commander* pour en discuter 👇"
        ),
    },
    "branding": {
        "keywords": ["5", "branding", "identité", "identite", "charte"],
        "response": (
            "✨ *Branding Complet*\n\n"
            "Identité visuelle complète:\n"
            "- Logo\n"
            "- Palette de couleurs\n"
            "- Typographie\n"
            "- Guidelines de marque\n\n"
            "💰 Tarif: sur devis\n"
            "Tape *commander* pour en discuter 👇"
        ),
    },
    "video": {
        "keywords": ["6", "video", "reels", "reel", "montage", "tiktok", "instagram"],
        "response": (
            "🎬 *Montage Vidéo / Reels*\n\n"
            "Reels Instagram, TikTok et vidéos promos.\n\n"
            "💰 Tarif: sur devis\n"
            "⏱️ Délai: 24h-72h selon le projet\n\n"
            "Tape *commander* pour en discuter 👇"
        ),
    },
    "prix": {
        "keywords": ["prix", "tarif", "tarifs", "combien", "cout", "coût", "price"],
        "response": (
            "💰 *Tarifs Komara Agency*\n\n"
            "🎨 Logo pro: 300k - 500k GNF\n"
            "🖼️ Affiche/Flyer: 300k GNF\n"
            "📸 Retouche photo: sur discussion\n"
            "🤖 Bots: sur devis\n"
            "✨ Branding: sur devis\n"
            "🎬 Montage vidéo: sur devis\n\n"
            "✅ 2 révisions gratuites\n"
            "💰 Révision sup: 50k GNF\n"
            "⚡ Express 24h: +30%\n"
            "💳 Paiement: Orange Money, MTN, Virement, PayPal"
        ),
    },
    "commander": {
        "keywords": ["commander", "commande", "je veux", "je prends", "ok je prends"],
        "response": (
            "Super ! 🚀 Pour lancer ta commande, j'ai besoin de:\n\n"
            "1. Le type de projet (logo, affiche, etc.)\n"
            "2. Une description de ce que tu veux\n"
            "3. Ton délai souhaité (normal ou express 24h)\n\n"
            "Écris-moi les détails ici 👇"
        ),
    },
    "paiement": {
        "keywords": ["paiement", "payer", "payment", "orange money", "mtn", "virement", "paypal"],
        "response": (
            "💳 *Modes de paiement*\n\n"
            "1. Orange Money\n"
            "2. MTN Money\n"
            "3. Virement bancaire\n"
            "4. PayPal\n\n"
            "Le paiement se fait après validation du devis.\n"
            "Tape *commander* pour commencer 👇"
        ),
    },
    "delai": {
        "keywords": ["délai", "delai", "quand", "combien de temps", "rapide"],
        "response": (
            "⏱️ *Délais de livraison*\n\n"
            "Normal: 24h-72h selon le projet\n"
            "Express 24h: +30% sur le tarif\n\n"
            "Le délai commence après validation du devis et paiement."
        ),
    },
    "revision": {
        "keywords": ["révision", "revision", "modifier", "changer", "correction"],
        "response": (
            "✏️ *Révisions*\n\n"
            "2 révisions gratuites incluses.\n"
            "Révision supplémentaire: 50k GNF\n\n"
            "Dis-moi ce que tu veux modifier 👇"
        ),
    },
    "contact": {
        "keywords": ["contact", "téléphone", "telephone", "numéro", "numero", "appel"],
        "response": (
            "📞 *Contact Komara Agency*\n\n"
            "WhatsApp: +212 701-986219\n"
            "Email: komara.agency@gmail.com\n"
            "Portfolio: https://ndinekomara2442-cmd.github.io/komara-agency-portfolio/\n\n"
            "Disponible 7j/7 de 8h à 22h (GMT)"
        ),
    },
    "merci": {
        "keywords": ["merci", "thanks", "thank you", "ok merci", "super merci"],
        "response": (
            "Avec plaisir ! 😊\n"
            "N'hésite pas si tu as d'autres questions.\n\n"
            "Komara Agency 🇬🇳 — Vision. Impact. Excellence."
        ),
    },
    "default": {
        "keywords": [],
        "response": (
            "Je n'ai pas bien compris 🤔\n\n"
            "Tape un mot-clé:\n"
            "1. Logo\n"
            "2. Affiche\n"
            "3. Retouche photo\n"
            "4. Bots\n"
            "5. Branding\n"
            "6. Montage vidéo\n\n"
            "Ou tape *prix*, *commander*, *contact* 👇"
        ),
    },
}


# ==================== LOGIQUE DU BOT ====================

class KomaraBot:
    """Bot WhatsApp Business pour Komara Agency"""

    def __init__(self, config: Dict = BOT_CONFIG):
        self.config = config
        self.responses = CANNED_RESPONSES
        self.conversation_state: Dict[str, str] = {}  # user_id -> state

    def match_response(self, message: str) -> str:
        """Trouve la meilleure réponse selon le message reçu"""
        msg_lower = message.lower().strip()

        # Si l'utilisateur est en mode "commande", on stocke les détails
        user_state = self.conversation_state.get("current_user", "")
        if user_state == "awaiting_order_details":
            self.conversation_state["current_user"] = ""
            return (
                "Parfait ! J'ai bien noté ta demande ✅\n\n"
                "Je te réponds rapidement avec un devis personnalisé.\n"
                "Délai de réponse: moins de 2h pendant les heures d'ouverture.\n\n"
                "Komara Agency 🇬🇳"
            )

        # Recherche par mots-clés
        for key, data in self.responses.items():
            if key == "default":
                continue
            for keyword in data["keywords"]:
                if keyword in msg_lower:
                    if key == "commander":
                        self.conversation_state["current_user"] = "awaiting_order_details"
                    return data["response"]

        return self.responses["default"]["response"]

    def get_welcome_message(self) -> str:
        """Message de bienvenue pour nouveaux clients"""
        return self.responses["welcome"]["response"]

    def get_away_message(self, current_hour: int = None) -> str:
        """Message d'absence selon l'heure"""
        if current_hour is None:
            current_hour = datetime.datetime.now().hour

        if current_hour < 8 or current_hour >= 22:
            return (
                "🌙 *Komara Agency — Hors ligne*\n\n"
                "Je suis actuellement indisponible.\n"
                "Heures d'ouverture: 8h - 22h (GMT)\n\n"
                "Laisse-moi ton message, je te réponds dès que possible ! 👋"
            )
        return None

    def get_follow_up_reminder(self, client_name: str, project_type: str, reminder_type: str) -> str:
        """Génère un message de relance personnalisé"""
        templates = {
            "Paiement J+1": (
                f"Bonjour {client_name} 👋\n\n"
                f"Petit rappel concernant ton projet *{project_type}*.\n"
                f"Le paiement est attendu pour finaliser la livraison.\n\n"
                f"💳 Modes de paiement:\n"
                f"1. Orange Money\n"
                f"2. MTN Money\n"
                f"3. Virement bancaire\n"
                f"4. PayPal\n\n"
                f"Merci de ton confiance ! 🇬🇳"
            ),
            "Hésitant J+5": (
                f"Bonjour {client_name} 👋\n\n"
                f"Je fais suite à notre échange concernant ton projet *{project_type}*.\n"
                f"Tu as encore des questions ou des hésitations ?\n\n"
                f"Je suis dispo pour en discuter, n'hésite pas ! 😊"
            ),
            "Suivi satisfaction J+7": (
                f"Bonjour {client_name} 👋\n\n"
                f"Tu as reçu ta commande *{project_type}* il y a quelques jours.\n"
                f"J'espère que ça te plaît ! 😊\n\n"
                f"N'hésite pas à me dire si tu as besoin d'ajustements.\n"
                f"Ton avis compte beaucoup pour moi 🙏"
            ),
            "Aucun": "",
        }
        return templates.get(reminder_type, templates["Paiement J+1"])


# ==================== EXEMPLE D'UTILISATION ====================

if __name__ == "__main__":
    bot = KomaraBot()

    # Simulation de messages
    test_messages = [
        "Salam",
        "1",           # Logo
        "prix",
        "commander",
        "Je veux un logo pour mon restaurant",
        "merci",
    ]

    print("=" * 50)
    print(f"🤖 {BOT_CONFIG['agency_name']} Bot — Test")
    print("=" * 50)

    for msg in test_messages:
        print(f"\n👤 Client: {msg}")
        response = bot.match_response(msg)
        print(f"🤖 Bot: {response}")
        print("-" * 50)

    # Test message d'absence
    print(f"\n🌙 Test away message (3h du matin):")
    away = bot.get_away_message(current_hour=3)
    print(away)

    # Test relance
    print(f"\n📩 Test relance:")
    reminder = bot.get_follow_up_reminder(
        client_name="Mamadou",
        project_type="Logo restaurant",
        reminder_type="Paiement J+1"
    )
    print(reminder)

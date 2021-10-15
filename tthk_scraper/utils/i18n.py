from tthk_scraper.models.change.status import Status

ESTONIAN_STATUS_TRIGGERS = {
    "lõuna": Status.Lunch,
    "jääb ära": Status.DroppedOut,
    "söögivahetund": Status.Lunch,
    "iseseisev ülesanne kodus": Status.Homework,
    "iseseisev töö kodus": Status.Homework,
    "tunnid toimuvad": Status.Scheduled
}

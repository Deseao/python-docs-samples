# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This file contains code samples that demonstrate how to get create IAM key for service account.

# [START iam_create_key]
def iam_create_key(project_id: str, email: str) -> None:
    from google.cloud import iam_admin_v1
    from google.cloud.iam_admin_v1 import types
    """
    Creates a key for a service account.

    project_id: ID or number of the Google Cloud project you want to use.
    email:
    """

    iam_admin_client = iam_admin_v1.IAMClient()
    request = types.CreateServiceAccountKeyRequest()

    request.name = f"projects/{project_id}/serviceAccounts/{email}"

    key = iam_admin_client.create_service_account_key(request=request)

    # The private_key_data field contains the stringified service account key
    # in JSON format. You cannot download it again later.
    # import json
    # json_key_file = json.loads(response.private_key_data)

    if not key.disabled:
        print("Created json key")


if __name__ == "__main__":
    # To run the sample you would need
    # iam.serviceAccountKeys.create permission (roles/iam.serviceAccountKeyAdmin)

    # Your Google Cloud project ID.
    project_id = "your-google-cloud-project-id"
    # Existing service account name within the project specified above.
    account_name = "your-service-account-name"
    # Note: If you have different email format, you can just paste it directly
    email = f"{account_name}@{project_id}.iam.gserviceaccount.com"

    iam_create_key(project_id, email)


# [END iam_create_key]
